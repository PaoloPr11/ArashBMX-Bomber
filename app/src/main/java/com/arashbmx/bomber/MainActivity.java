package com.arashbmx.bomber;

import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebChromeClient;
import android.webkit.WebViewClient;
import android.webkit.JavascriptInterface;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Handler;
import android.os.Looper;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import android.view.KeyEvent;

public class MainActivity extends AppCompatActivity {
    private WebView webView;
    private ExecutorService executor = Executors.newSingleThreadExecutor();
    private Handler mainHandler = new Handler(Looper.getMainLooper());
    private boolean isRunning = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        webView = findViewById(R.id.webView);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.getSettings().setDomStorageEnabled(true);
        webView.getSettings().setAllowFileAccess(true);
        webView.getSettings().setAllowContentAccess(true);
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                return false;
            }
        });
        webView.setWebChromeClient(new WebChromeClient());
        webView.addJavascriptInterface(new AndroidBridge(), "AndroidBridge");
        webView.loadUrl("file:///android_asset/www/index.html");
    }
    
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (keyCode == KeyEvent.KEYCODE_BACK) {
            webView.loadUrl("javascript:if(confirm('خروج از برنامه؟')){window.AndroidBridge.exitApp();}");
            return true;
        }
        return super.onKeyDown(keyCode, event);
    }

    private class AndroidBridge {
        @JavascriptInterface
        public void startAttack(final String phone, final int rounds) {
            if (isRunning) return;
            isRunning = true;
            
            executor.execute(() -> {
                try {
                    // واردات پایتون
                    final Class<?> bomberClass = Class.forName("com.arashbmx.bomber.Bomber");
                    final Object bomber = bomberClass.getConstructor(String.class).newInstance(phone);
                    final java.lang.reflect.Method getServices = bomberClass.getMethod("get_services");
                    final java.util.List<?> services = (java.util.List<?>) getServices.invoke(bomber);
                    
                    final int total = services.size() * rounds;
                    final int[] success = {0};
                    final int[] count = {0};
                    
                    mainHandler.post(() -> 
                        webView.loadUrl("javascript:window.AndroidBridge.onLog('🚀 شروع حمله به "+phone+"', 'log-info')")
                    );
                    
                    for (int r=1; r<=rounds; r++) {
                        final int round = r;
                        mainHandler.post(() -> 
                            webView.loadUrl("javascript:window.AndroidBridge.onLog('🔄 دور "+round+"/"+rounds+"', 'log-info')")
                        );
                        
                        for (Object svcObj : services) {
                            java.util.Map<?, ?> svc = (java.util.Map<?, ?>) svcObj;
                            final String name = (String) svc.get("name");
                            final Object func = svc.get("func");
                            
                            if (func instanceof java.lang.reflect.Method) {
                                java.lang.reflect.Method method = (java.lang.reflect.Method) func;
                                int code = (int) method.invoke(bomber);
                                count[0]++;
                                if (code == 200 || code == 201 || code == 202 || code == 204) {
                                    success[0]++;
                                }
                                
                                final int fCode = code;
                                final int fCount = count[0];
                                final int fSuccess = success[0];
                                final boolean ok = (code == 200 || code == 201 || code == 202 || code == 204);
                                
                                mainHandler.post(() -> {
                                    String icon = ok ? "✅" : "❌";
                                    String cls = ok ? "log-ok" : "log-no";
                                    webView.loadUrl("javascript:window.AndroidBridge.onLog('"+icon+" "+name+" ["+fCode+"]', '"+cls+"')");
                                    int pct = (int)((fCount * 100.0) / total);
                                    webView.loadUrl("javascript:window.AndroidBridge.onProgress("+pct+")");
                                });
                                
                                Thread.sleep(150);
                            }
                        }
                        
                        if (r < rounds) {
                            Thread.sleep(1000);
                        }
                    }
                    
                    final int finalSuccess = success[0];
                    final int finalTotal = total;
                    mainHandler.post(() -> {
                        double rate = (finalSuccess * 100.0 / finalTotal);
                        webView.loadUrl("javascript:window.AndroidBridge.onLog('═══════════════════════════', 'log-summary')");
                        webView.loadUrl("javascript:window.AndroidBridge.onLog('📊 کل: "+finalTotal+"', 'log-summary')");
                        webView.loadUrl("javascript:window.AndroidBridge.onLog('✅ موفق: "+finalSuccess+"', 'log-ok')");
                        webView.loadUrl("javascript:window.AndroidBridge.onLog('📈 نرخ: "+String.format("%.1f", rate)+"%', 'log-info')");
                        webView.loadUrl("javascript:window.AndroidBridge.onLog('═══════════════════════════', 'log-summary')");
                        webView.loadUrl("javascript:window.AndroidBridge.onFinish()");
                        isRunning = false;
                    });
                    
                } catch (Exception e) {
                    e.printStackTrace();
                    final String error = e.getMessage() != null ? e.getMessage() : "Unknown error";
                    mainHandler.post(() -> {
                        webView.loadUrl("javascript:window.AndroidBridge.onLog('❌ خطا: "+error.replace("'", "\\'")+"', 'log-no')");
                        webView.loadUrl("javascript:window.AndroidBridge.onFinish()");
                        isRunning = false;
                    });
                }
            });
        }
        
        @JavascriptInterface
        public void exitApp() {
            finish();
        }
    }
}
