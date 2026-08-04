let isRunning = false;

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('startBtn').addEventListener('click', startAttack);
    document.getElementById('exitBtn').addEventListener('click', function() {
        if (confirm('خروج از برنامه؟')) {
            if (window.AndroidBridge) {
                window.AndroidBridge.exitApp();
            } else {
                window.close();
            }
        }
    });
    document.getElementById('phone').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') startAttack();
    });
});

function addLog(text, cls = '') {
    const log = document.getElementById('logArea');
    const div = document.createElement('div');
    div.textContent = text;
    if (cls) div.className = cls;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
}

function updateProgress(percent) {
    document.getElementById('progressBar').style.width = Math.min(100, percent) + '%';
}

function startAttack() {
    if (isRunning) return;
    
    const phone = document.getElementById('phone').value.trim();
    if (!phone || phone.length < 10) {
        addLog('❌ شماره معتبر وارد کنید (09xxx)', 'log-no');
        return;
    }
    
    let cleanPhone = phone;
    if (cleanPhone.startsWith('09') && cleanPhone.length === 11) {
        // ok
    } else if (cleanPhone.startsWith('9') && cleanPhone.length === 10) {
        cleanPhone = '0' + cleanPhone;
    } else if (cleanPhone.length === 10 && !cleanPhone.startsWith('0')) {
        cleanPhone = '0' + cleanPhone;
    } else if (cleanPhone.length === 11 && cleanPhone.startsWith('0')) {
        // ok
    } else {
        addLog('❌ فرمت شماره صحیح نیست', 'log-no');
        return;
    }
    
    const rounds = parseInt(document.getElementById('rounds').value);
    const btn = document.getElementById('startBtn');
    btn.disabled = true;
    btn.textContent = '⏳ در حال اجرا...';
    isRunning = true;
    
    document.getElementById('logArea').innerHTML = '';
    updateProgress(0);
    
    if (window.AndroidBridge) {
        window.AndroidBridge.startAttack(cleanPhone, rounds);
    } else {
        simulateAttack(cleanPhone, rounds);
    }
}

function attackFinished() {
    const btn = document.getElementById('startBtn');
    btn.disabled = false;
    btn.textContent = '🚀 START ATTACK';
    isRunning = false;
}

window.AndroidBridge = {
    onLog: function(msg, type) {
        addLog(msg, type);
    },
    onProgress: function(pct) {
        updateProgress(pct);
    },
    onFinish: function() {
        attackFinished();
    },
    exitApp: function() {
        // توسط جاوا مدیریت می‌شود
    }
};

function simulateAttack(phone, rounds) {
    const services = ['Gharar','Filimo','Divar','Tapsi','Digikala','Snapp','SnappFood','Alibaba','Rubika','Shad','Namava','Torob','Gap','Basalam','Filmnet','MrBilit','Jabama','Appetit','Karafs','Pindo','Tamasha','Behtarino','IApps','Unitech','Okala','SnappTrip','DrDr','Itoll','Azki','Nobat','Chamedoon','BaniMode','Lendo','Olgoo','Pakhsh','DideNegar','Buskool','Kilid','See5','Ghabzino','SimKhan','DrSaina','Binjo','Limome','Bimito','SeeBirani','MihanPezeshk','Hamrah','Telewebion','Echarge','Shad','Rubika','Emtiaz','GapFilm','Sheypoor','AbarKelas','ArzDigital','FilimoSchool','Anargift','BimitoVip'];
    
    let total = 0, success = 0;
    const totalReqs = services.length * rounds;
    
    function doRound(r) {
        if (r > rounds) {
            const rate = (success / total * 100).toFixed(1);
            addLog('═══════════════════════════', 'log-summary');
            addLog(`📊 کل درخواست‌ها: ${total}`, 'log-summary');
            addLog(`✅ موفق: ${success}`, 'log-ok');
            addLog(`📈 نرخ موفقیت: ${rate}%`, 'log-info');
            addLog('═══════════════════════════', 'log-summary');
            attackFinished();
            return;
        }
        
        addLog(`🔄 دور ${r}/${rounds}`, 'log-info');
        let idx = 0;
        
        function doService() {
            if (idx >= services.length) {
                setTimeout(() => doRound(r + 1), 1500);
                return;
            }
            const svc = services[idx];
            idx++;
            const ok = Math.random() > 0.2;
            total++;
            if (ok) success++;
            const code = ok ? 200 : 404;
            addLog(`${ok ? '✅' : '❌'} ${svc} [${code}]`, ok ? 'log-ok' : 'log-no');
            const pct = (total / totalReqs) * 100;
            updateProgress(pct);
            setTimeout(doService, 300);
        }
        doService();
    }
    doRound(1);
}
