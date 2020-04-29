import requests
from bs4 import BeautifulSoup
from datetime import datetime




class veri_cekme(object):

    def link_ayir(self):
        url = "https://altin.doviz.com/"
        request = requests.get(url)
        cevap = request.content
        soup = BeautifulSoup(cevap, "lxml")
        self.db = []
        kur = []
        sayac = 0
        self.parite = 0
        for data1 in soup.find_all("td", {"style": "text-align:right;"}):
            data1 = data1.text.replace(",", ".")
            kur.append(data1)
            sayac += 1
            if sayac == 32:
                return kur
 
        return kur


    def link_ayir_kur(self):
        url = "https://kur.doviz.com/"
        request = requests.get(url)
        cevap = request.content
        soup = BeautifulSoup(cevap, "lxml")
        self.db = []
        kur = []
        self.parite = 0
        for data in soup.find_all("div", {"class": "kur-page kur-list"}):

            for data1 in data.find_all("td", {"style": "text-align:right;"}):
                data1 = data1.text.replace(",", ".")
                kur.append(data1)
        return kur


    def time(self):
        now = datetime.now()
        now = now.strftime("%X")
        return now


keys = [
'USDALIS', 'USDSATIS', 'USDYUKSEK', 'USDDUSUK', 'EURALIS', 'EURSATIS', 'EURYUKSEK', 'EURDUSUK', 'GBPALIS', 'GBPSATIS', 'GBPYUKSEK', 'GBPDUSUK', 'CHFALIS', 'CHFSATIS', 'CHFYUKSEK', 'CHFDUSUK',
'CADALIS', 'CADSATIS', 'CADYUKSEK', 'CADDUSUK', 'RUBALIS', 'RUBSATIS', 'RUBYUKSEK', 'RUBDUSUK', 'AEDALIS', 'AEDSATIS', 'AEDYUKSEK', 'AEDDUSUK', 'AUDALIS', 'AUDSATIS', 'AUDYUKSEK', 'AUDDUSUK',
'DKKALIS', 'DKKSATIS', 'DKKYUKSEK', 'DKKDUSUK', 'SEKALIS', 'SEKSATIS', 'SEKYUKSEK', 'SEKDUSUK', 'NOKALIS', 'NOKSATIS', 'NOKYUKSEK', 'NOKDUSUK', 'JPYALIS', 'JPYSATIS', 'JPYYUKSEK', 'JPYDUSUK',
'KWDALIS', 'KWDSATIS', 'KWDYUKSEK', 'KWDDUSUK', 'ZARALIS', 'ZARSATIS', 'ZARYUKSEK', 'ZARDUSUK', 'BHDALIS', 'BHDSATIS', 'BHDYUKSEK', 'BHDDUSUK', 'LYDALIS', 'LYDSATIS', 'LYDYUKSEK', 'LYDDUSUK',
'SARALIS', 'SARSATIS', 'SARYUKSEK', 'SARDUSUK', 'IQDALIS', 'IQDSATIS', 'IQDYUKSEK', 'IQDDUSUK', 'ILSALIS', 'ILSSATIS', 'ILSYUKSEK', 'ILSDUSUK', 'IRRALIS', 'IRRSATIS', 'IRRYUKSEK', 'IRRDUSUK',
'INRALIS', 'INRSATIS', 'INRYUKSEK', 'INRDUSUK', 'MXNALIS', 'MXNSATIS', 'MXNYUKSEK', 'MXNDUSUK', 'HUFALIS', 'HUFSATIS', 'HUFYUKSEK', 'HUFDUSUK', 'NZDALIS', 'NZDSATIS', 'NZDYUKSEK', 'NZDDUSUK',
'BRLALIS', 'BRLSATIS', 'BRLYUKSEK', 'BRLDUSUK', 'IDRALIS', 'IDRSATIS', 'IDRYUKSEK', 'IDRDUSUK', 'CSKALIS', 'CSKSATIS', 'CSKYUKSEK', 'CSKDUSUK', 'PLNALIS', 'PLNSATIS', 'PLNYUKSEK', 'PLNDUSUK',
'RONALIS', 'RONSATIS', 'RONYUKSEK', 'RONDUSUK', 'CNYALIS', 'CNYSATIS', 'CNYYUKSEK', 'CNYDUSUK', 'ARSALIS', 'ARSSATIS', 'ARSYUKSEK', 'ARSDUSUK', 'ALLALIS', 'ALLSATIS', 'ALLYUKSEK', 'ALLDUSUK',
'AZNALIS', 'AZNSATIS', 'AZNYUKSEK', 'AZNDUSUK', 'BAMALIS', 'BAMSATIS', 'BAMYUKSEK', 'BAMDUSUK', 'CLPALIS', 'CLPSATIS', 'CLPYUKSEK', 'CLPDUSUK', 'COPALIS', 'COPSATIS', 'COPYUKSEK', 'COPDUSUK',
'CRCALIS', 'CRCSATIS', 'CRCYUKSEK', 'CRCDUSUK', 'DZDALIS', 'DZDSATIS', 'DZDYUKSEK', 'DZDDUSUK', 'EGPALIS', 'EGPSATIS', 'EGPYUKSEK', 'EGPDUSUK', 'HKDALIS', 'HKDSATIS', 'HKDYUKSEK', 'HKDDUSUK',
'HRKALIS', 'HRKSATIS', 'HRKYUKSEK', 'HRKDUSUK', 'ISKALIS', 'ISKSATIS', 'ISKYUKSEK', 'ISKDUSUK', 'JODALIS', 'JODSATIS', 'JODYUKSEK', 'JODDUSUK', 'KRWALIS', 'KRWSATIS', 'KRWYUKSEK', 'KRWDUSUK',
'KZTALIS', 'KZTSATIS', 'KZTYUKSEK', 'KZTDUSUK', 'LBPALIS', 'LBPSATIS', 'LBPYUKSEK', 'LBPDUSUK', 'LKRALIS', 'LKRSATIS', 'LKRYUKSEK', 'LKRDUSUK', 'MADALIS', 'MADSATIS', 'MADYUKSEK', 'MADDUSUK',
'MDLALIS', 'MDLSATIS', 'MDLYUKSEK', 'MDLDUSUK', 'MKDALIS', 'MKDSATIS', 'MKDYUKSEK', 'MKDDUSUK', 'MYRALIS', 'MYRSATIS', 'MYRYUKSEK', 'MYRDUSUK', 'OMRALIS', 'OMRSATIS', 'OMRYUKSEK', 'OMRDUSUK',
'PENALIS', 'PENSATIS', 'PENYUKSEK', 'PENDUSUK', 'PHPALIS', 'PHPSATIS', 'PHPYUKSEK', 'PHPDUSUK', 'PKRALIS', 'PKRSATIS', 'PKRYUKSEK', 'PKRDUSUK', 'QARALIS', 'QARSATIS', 'QARYUKSEK', 'QARDUSUK',
'RSDALIS', 'RSDSATIS', 'RSDYUKSEK', 'RSDDUSUK', 'SGDALIS', 'SGDSATIS', 'SGDYUKSEK', 'SGDDUSUK', 'SYPALIS', 'SYPSATIS', 'SYPYUKSEK', 'SYPDUSUK', 'THBALIS', 'THBSATIS', 'THBYUKSEK', 'THBDUSUK',
'TWDALIS', 'TWDSATIS', 'TWDYUKSEK', 'TWDDUSUK', 'UAHALIS', 'UAHSATIS', 'UAHYUKSEK', 'UAHDUSUK', 'UYUALIS', 'UYUSATIS', 'UYUYUKSEK', 'UYUDUSUK', 'GELALIS', 'GELSATIS', 'GELYUKSEK', 'GELDUSUK'
]

keys2 = [
'ONSALIS', 'ONSSATIS', 'GRMALIS', 'GRMSATIS', 'CYRALIS', 'CYRSATIS', 'YRMALIS', 'YRMSATIS', 'TAMALIS', 'TAMSATIS', 'CMHALIS', 'CMHSATIS', 'ATAALIS', 'ATASATIS', 'RSTALIS', 'RSTSATIS', 'HMTALIS',
'HMTSATIS', 'IKIALIS', 'IKISATIS', 'GRSALIS', 'GRSSATIS', 'BESALIS', 'BESSATIS', '14ALIS', '14SATIS', '18ALIS', '18SATIS', '22ALIS', '22SATIS', 'GMSALIS', 'GMSSATIS'  
]




