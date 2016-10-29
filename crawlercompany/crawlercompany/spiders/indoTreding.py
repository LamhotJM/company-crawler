from scrapy.selector import Selector
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
        import  string
        printable = set(string.printable)
        totalPage = url.xpath(
            "//*[@id='ContentPlaceHolder1_pager']/div/div/ul/li/a/text()|//*/a/b/text()").extract()
        totalPageValue = totalPage if totalPage else ''
        totalPageValue= filter(lambda x: x in printable, totalPageValue)
        cleanList = [str(item) for item in totalPageValue]
        pageCount=max(cleanList)
        with open('test.txt', 'a') as f:
            f.write('{0};{1}\n'.format(response.url, str(pageCount)))


