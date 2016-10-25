from scrapy.selector import Selector
from scrapy.item import Field, Item
from scrapy.http import Request
import scrapy


class IndoTrndingMySpider(scrapy.Spider):
    name = "indo_test"
    allowed_domains = ["indotrading.com"]
    start_urls = [
        'https://www.indotrading.com/services/desaininterior/',
        'https://www.indotrading.com/services/kontraktor-bangunan/',
        'https://www.indotrading.com/services/agenproperti/',
        'https://www.indotrading.com/services/arsitektur/',
        'https://www.indotrading.com/services/kontraktorbaja/',
        'https://www.indotrading.com/services/kontraktor-rumah/',
        'https://www.indotrading.com/services/kontraktor-kolam-renang/',
        'https://www.indotrading.com/services/kontraktor-sipil/',
        'https://www.indotrading.com/services/sewa-alat-konstruksi/',
        'https://www.indotrading.com/services/jasa-pengeboran/',
        'https://www.indotrading.com/services/jasa-geologi/',
        'https://www.indotrading.com/services/pembangkit-listrik/',
        'https://www.indotrading.com/services/kargo-dan-logistik/',
        'https://www.indotrading.com/services/jasa-pindahan/',
        'https://www.indotrading.com/services/travel-agent/',
        'https://www.indotrading.com/services/rentalkendaraan/',
        'https://www.indotrading.com/services/sewa-villa/',
        'https://www.indotrading.com/services/waralaba/',
        'https://www.indotrading.com/services/konsultanpajak/',
        'https://www.indotrading.com/services/konsultan-bisnis/',
        'https://www.indotrading.com/services/agen-asuransi/',
        'https://www.indotrading.com/services/layanan-keuangan/',
        'https://www.indotrading.com/services/notaris/',
        'https://www.indotrading.com/services/headhunter/',
        'https://www.indotrading.com/services/jasa-percetakan/',
        'https://www.indotrading.com/services/jasa-penerjemah/',
        'https://www.indotrading.com/services/konsultan-hukum-dan-pengacara/',
        'https://www.indotrading.com/services/outsourcing/',
        'https://www.indotrading.com/services/perusahaan-akuntansi/',
        'https://www.indotrading.com/services/penulis/',
        'https://www.indotrading.com/services/bahasaasing/',
        'https://www.indotrading.com/services/kursus-tari/',
        'https://www.indotrading.com/services/penjahit-pakaian/',
        'https://www.indotrading.com/services/studio-foto/',
        'https://www.indotrading.com/services/jasapenerbitan/',
        'https://www.indotrading.com/services/layanankesehatan/',
        'https://www.indotrading.com/services/salon/',
        'https://www.indotrading.com/services/ahli-gizi/',
        'https://www.indotrading.com/services/penampilanmusikorkestra/',
        'https://www.indotrading.com/services/layananbartending/',
        'https://www.indotrading.com/services/laundry/',
        'https://www.indotrading.com/services/tukangtaman/',
        'https://www.indotrading.com/services/kursus-menjahit/',
        'https://www.indotrading.com/services/kursus-mengemudi/',
        'https://www.indotrading.com/services/kursus-kecantikan/',
        'https://www.indotrading.com/services/pijat-refleksi/',
        'https://www.indotrading.com/services/bimbingan-belajar/',
        'https://www.indotrading.com/services/pelayanan-rumah-tangga/',
        'https://www.indotrading.com/services/kursus-kerajinan-tangan/',
        'https://www.indotrading.com/services/beauty-center/',
        'https://www.indotrading.com/services/reparasielektronik/',
        'https://www.indotrading.com/services/jasalassolder/',
        'https://www.indotrading.com/services/sewa-alat-kantor/',
        'https://www.indotrading.com/services/bengkel-mobil/',
        'https://www.indotrading.com/services/bengkel-motor/',
        'https://www.indotrading.com/services/teknisi-ac/',
        'https://www.indotrading.com/services/teknisi-listrik/',
        'https://www.indotrading.com/services/teknisi-mekanik/',
        'https://www.indotrading.com/services/kalibrasi/',
        'https://www.indotrading.com/services/jasa-desain-grafis/',
        'https://www.indotrading.com/services/perusahaan-it/',
        'https://www.indotrading.com/services/training-komputer-dan-it/',
        'https://www.indotrading.com/services/training-komunikasi/',
        'https://www.indotrading.com/services/kursus-fotografi/',
        'https://www.indotrading.com/services/kursus-manajemen/',
        'https://www.indotrading.com/services/eventorganizer/',
        'https://www.indotrading.com/services/jasapembuatanfilm/',
        'https://www.indotrading.com/services/katering/',
        'https://www.indotrading.com/services/agen-iklan/',
        'https://www.indotrading.com/services/pertukangan/',
        'https://www.indotrading.com/services/jasa-instalasi/',
        'https://www.indotrading.com/services/jasa-perbaikan/',
    ]

    def parse(self, response):
        url = Selector(response)
        rootElement = url.xpath(".//*[@id='form1']/div/div/div[1]/div/ul/li/div/div/ul/li")
        # //*[@id="form1"]/div[3]/div[2]/div[3]/div/div[1]/div

        import time
        for subRoot in rootElement:
            url_cat = subRoot.xpath(".//a/@href").extract()
            url_cat = url_cat[0].strip() if url_cat  else ''
            import re
            htmlspaced = re.sub(r" ", "", url_cat)

            # yield Request(url=url_cat, callback=self.ParseTotalPage, dont_filter=True)
            with open('test2.txt', 'a') as f:
                f.write('{0}\n'.format(htmlspaced))

    def ParseTotalPage(self, response):
        url = Selector(response)
        totalPage = url.xpath(
            "//*[@id='ContentPlaceHolder1_pager']/div/div/ul/li/a/text()|//*/div/div/ul/li/a/b/text()").extract()
        totalPageValue = totalPage[0].strip() if totalPage  else ''

        with open('test.txt', 'a') as f:
            f.write('{0};{1}\n'.format(response.url, totalPageValue))
