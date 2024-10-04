import vertexai
import os
from vertexai.generative_models import GenerativeModel

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = " your Service Account"

def init_cs_bot_session():
    # Custom context to focus on Kabinet Baskara HIMA IF 2024 without unnecessary phrases
    context = """
    Kamu adalah AI yang bertugas memberikan informasi tentang Kabinet Baskara HIMA IF Universitas Telkom 2024. Jawabanmu harus jelas, langsung, dan tidak menggunakan frasa seperti "Berdasarkan informasi yang kamu berikan" atau "Seperti yang telah disebutkan." Fokus hanya memberikan informasi yang relevan, tepat, dan to the point.
    
    Berikut adalah beberapa informasi kunci tentang Kabinet Baskara HIMA IF 2024:
    HIMPUNAN MAHASISWA
S1 INFORMATIKA
HIMA IF Universitas Telkom adalah organisasi yang bersifat keprofesian di bidang informatika dan berdasarkan Tridharma Perguruan Tinggi yang berlandaskan Pancasila                                                                                                                            
HIMA IF Universitas Telkom didirikan pada tanggal 10 Desember 2014 (yang sebelumnya bernama HMIF IT Telkom didirikan pada tanggal 14 Juli 1993) di Bandung sampai dengan waktu yang tidak ditentukan.                                                                                                                        
                            Kahim																							
                            Ariq Atmaja Deza																							
                                                                                                                        
                            Wakahim																							
                            Rasendriya Abel																							
                                                                                                                        
                Sekretaris 1	Sekretaris 2		  		Bendahara 1	Bendahara 2																				
                Salma Atika	Chantika Anasthya				Raisya Azzuhra	Qualifia Nayyara																				
                                                                                                                        
                                                                                                                        
                Kadep Internal			Kadep PSDM			Kadep Eksternal																				
                Gatien Naufal 			Rafhiromadoni Sopandi			Naufal Dzakwan																				
                                                                                                                        
                                                                                                                        
            Divisi KMS	Divisi BNK		Divisi KDR	Divisi MNB	Divisi ARK		Divisi RKS	Divisi MIK																			
            Kadiv	Kadiv		Kadiv	Kadiv	Kadiv		Kadiv	Kadiv																			
            Argiansyah Galih	Naufal  Pratama		Mahardhika Fernanda	Fatah Fadhlur 	Alexander Raditya		Khavin Edsyah	M Agung Gustiansyah																			
            Wakadiv	Wakadiv		Wakadiv	Wakadiv	Wakadiv		Wakadiv	Wakadiv																			
            Deborah Fransiska	Chatelia Pramesti		Nadiella Fitantriani	Nabila Keiko	Aura Widiya		Grizelda Audria	Jauza Zahra Ulaya																			
                                                                                                                        
                                                                                                                        
                        SUPERINTI																								
                        SUPERINTI						 																		
                        JABATAN	NAMA	NIM				 																		
                        Ketua Himpunan	Ariq Atmaja Deza	1301220367																						
                        Wakil Ketua Himpunan	Rasendriya Abel Abhista Kristiawan	1301223149																						
                        Sekretaris Umum 1	Salma Atika Poerwadi	1301223068																						
                        Sekretaris Umum 2	Chantika Anasthya	1301223321			 																			
                        Bendahara Umum 1	Raisya Azzuhra	1301223130																						
                        Bendahara Umum 2	Qualifia Nayyara Ammarani	1301223160																						
                        Kepala Departemen Internal	Gatien Naufal Raihansah	1301223467																						
                        Kepala Departemen PSDM	Rafhiromadoni Sopandi	1301223345																						
                        Kepala Departemen Eksternal	Naufal Dzakwan Zakianto	1301223254																						
                                                                                                                        
                        DEPARTEMEN INTERNAL																								
                        KMS (Kemahasiswaan)																								
                        JABATAN	NAMA	NIM																						
                        Kepala Divisi	Argiansyah Galih Permata	1301223397																						
                        Wakil Kepala Divisi	Deborah Fransiska	1301220272																						
                        Staff Ahli	Alviko Pradipta Harianto	1301220317																						
                        Staff Ahli	Raihan Diaurrahman	1301223358																						
                        Staff Ahli	Faiq Misbah Yazdi	1301223228																						
                        Staff Ahli	Imelia Dhevita Sari	1301220048																						
                        Staff Ahli	Muhammad Alvito Naufal Hakim	1301223342																						
                        Staff Ahli	Thafhan Rizqan H F	1301223097																						
                        BNK (Bisnis & Kewirausahaan)																								
                        JABATAN	NAMA	NIM																						
                        Kepala Divisi	Mohammad Naufal Widi Pratama	1301223109																						
                        Wakil Kepala Divisi	Chatelia Dyah Prameswari	1301223320																						
                        Staff Ahli	Azmi Rizqullah Rabbani	1301223290																						
                        Staff Ahli	Adinda Laras Sri Rahtami	1301223253																						
                        Staff Ahli	Achmad Rafly Khatami Zain	1301223349																						
                        Staff Ahli	Alisha Anggranidi Salsabila	1301223026																						
                        Staff Ahli	Zahra Amiera Putri Sailendra	1301223225																						
                        Staff Ahli	Ghefin Indra	1301220133																						
                                                                                                                        
                        DEPARTEMEN EKSTERNAL																								
                        RKS (Relasi Eksternal)																								
                        JABATAN	NAMA	NIM																						
                        Kepala Divisi	Khavin Edsyah Putra	1301220011																						
                        Wakil Kepala Divisi	Grizelda Audria Wijaya	1301224249																						
                        Staff Ahli	Bijak Prasodjo	1301223233																						
                        Staff Ahli	Yesi Sukmawati	1301223031																						
                        Staff Ahli	Farah Saraswati	1301223401																						
                        Staff Ahli	Salsabilla Hidi	1301223231																						
                        Staff Ahli	Anak Agung Sagung Putri Wijayanti	1301223079																						
                        MIK (Media Informasi & Komunikasi)																								
                        JABATAN	NAMA	NIM																						
                        Kepala Divisi	Muh Agung Gustiansyah	1301223123																						
                        Wakil Kepala Divisi	Jauza Zahra Ulaya	1301224452																						
                        Staff Ahli	Yulia Adinda Yuda	1301223415																						
                        Staff Ahli	Azkha Mardiyan Muttaqien	1301223306																						
                        Staff Ahli	Rian Pramudya Amanda	1301220303																						
                        Staff Ahli	Puguh Aiman Ariyanto	1301223038																						
                        Staff Ahli	Dinda Desfira	1301223236																						
                        Staff Ahli	Mikail Ardyas Wibowo	1301223416																						
                                                                                                                        
                        DEPARTEMEN PSDM																								
                        KDR (Kaderisasi)																								
                        JABATAN	NAMA	NIM																						
                        Kepala Divisi	Mahardhika Fernanda	1301223191																						
                        Wakil Kepala Divisi	Nadiella Fitantriani Putri	1301223195																						
                        Staff Ahli	Alfrando Halleluja Leonardo Holle	1301223035																						
                        Staff Ahli	Eko Wahyu Setiawan	1301223135																						
                        Staff Ahli	Kayla Amalika	1301223302																						
                        Staff Ahli	Rheno Febrian Cholistyo	1301220188																						
                        Staff Ahli	Wisnu Gholimsyah	1301223305																						
                        Staff Ahli	Nazwa Betha Kirana	1301223235																						
                        MNB (Minat & Bakat)																								
                        JABATAN	NAMA	NIM																						
                        Kepala Divisi	Fatah Fadhlur Rohman FN	1301223298																						
                        Wakil Kepala Divisi	Nabila Keiko Aura Pasha	1301220267																						
                        Staff Ahli	Bintang Rizky	1301223104																						
                        Staff Ahli	Taufik Adi Wardana	1301223269																						
                        Staff Ahli	Arya Sabda Pujangga Siswanto	1301220355																						
                        Staff Ahli	Aaron Barrichello Pattinama	1301223337																						
                        Staff Ahli	Iqal Mahendra Laksono	1301223243																						
                        Staff Ahli	Nazhmi Ahmad Fauzan	1301223056																						
                        ARK (Akademik Riset & Keprofesian)																								
                        JABATAN	NAMA	NIM																						
                        Kepala Divisi	Alexander Raditya Nugrahatama	1301223152																						
                        Wakil Kepala Divisi	Aura Widiya Paramitha	1301220264																						
                        Staff Ahli	Labib Hakam Fauzi	1301223113																						
                        Staff Ahli	Najwa Aulia Aziza	1301223331																						
                        Staff Ahli	Hazna Hamida Saputri	1301220094																						
                        Staff Ahli	Yassmin Syaharah Juliaman	1301223459																						
                        Staff Ahli	Johnson Dharma Leman	1301223404																						
                        Staff Ahli	Christoper Daeng Kilantan	1301223402																						
                        Staff Ahli	Riodino Raihan	1301220413																						
                        Staff Ahli	Wisnu Satrio Agung	1301223456																						
        GRAND DESIGN
        BADAN PENGURUS HARIAN
        HIMA IF 2024
        I. Visi dan Misi
        A. Visi
        - HIMA IF berfokus pada sinergi dan keragaman untuk mendorong terjadinya
        kemajuan
        Kata Kunci:
        - Sinergi : Kolaborasi atau interaksi yang memberikan hasil yang lebih besar
        daripada gabungan kontribusi individu.
        - Keragaman : Variasi perbedaan dalam budaya, bahasa, agama, latar belakang,
        atau sifat-sifat lainnya yang membuat suatu kelompok menjadi beragam.
        - Kemajuan : Perkembangan atau perbaikan dari waktu ke waktu.
        B. Misi
        1. Integrity
        Mewujudkan HIMA IF yang memiliki konsistensi dan keteguhan yang tidak
        tergoyahkan serta selalu mempertanggungjawabkan setiap langkah yang
        dilakukan.
        2. Growth Ecosystem
        Menyediakan wadah aktualisasi diri serta pengembangan minat dan bakat bagi
        HIMA IF.
        3. Resilience
        Menciptakan lingkungan HIMA IF yang adaptif, inklusif, dan supportif.
        4. Resilience
        Menjalin kerja sama yang baik dengan pihak internal maupun eksternal.
        II. Struktur Organisasi & Fungsi
        A. Ketua dan Wakil Ketua Himpunan
        - Menjalankan roda organisasi pada Himpunan Mahasiswa S1 Informatika.
        - Merealisasikan visi berdasarkan misi yang telah direncanakan.
        - Memberikan arahan kepada sumber daya yang dimiliki.
        - Membuat keputusan besar/umum.
        - Melakukan koordinasi dengan birokrat Telkom University.
        - Bertanggung jawab terhadap jalannya alur kepengurusan BPH HIMA IF.
        GRAND DESIGN
        BADAN PENGURUS HARIAN
        HIMA IF 2024
        B. Sekretaris
        - Bertanggung jawab dan berkoordinasi kepada Ketua dan Wakil Ketua HIMA IF.
        - Bertanggung jawab dan berkoordinasi kepada Sekretaris masing-masing divisi
        BPH HIMA IF.
        - Membuat Standar Operasional Prosedur (SOP) Kesekretariatan BPH HIMA IF
        secara efektif.
        - Melakukan dokumentasi proposal, laporan pertanggungjawaban, persuratan
        masuk dan keluar BPH HIMA IF.
        - Merekap hasil rapat rapat Inti dan rapat pleno BPH HIMA IF.
        - Merekap jadwal program kerja BPH HIMA IF.
        C. Bendahara
        - Bertanggung jawab dan berkoordinasi kepada Ketua dan Wakil Ketua HIMA IF.
        - Bertanggung jawab dan berkoordinasi kepada Bendahara masing-masing divisi
        BPH HIMA IF.
        - Melakukan audit keuangan BPH HIMA IF.
        - Membuat Standar Operasional Prosedur (SOP) Kebendaharaan BPH HIMA IF
        secara efektif.
        - Membuat dokumentasi laporan keuangan secara berkala dan transparan.
        - Mengelola keuangan BPH HIMA IF.
        D. Kepala Departemen
        - Bertanggung jawab dan berkoordinasi kepada Ketua dan Wakil Ketua HIMA IF.
        - Bertanggung jawab dalam pengembangan kompetensi keorganisasian dan
        pengelolaan sumber daya manusia untuk meningkatkan kualitas kerja terhadap
        seluruh anggota BPH HIMA IF.
        - Bertanggung jawab dalam menjaga kondisi internal dan memelihara kondusifitas
        lingkungan kerja BPH HIMA IF dengan pemberian motivasi, pelaksanaan fungsi
        apresiasi dan menciptakan nuansa kekeluargaan.
        - melakukan evaluasi secara berkala dan membuat laporan penilaian terhadap
        perkembangan kompetensi internal BPH HIMA IF.
        - Mengoordinasikan kegiatan rapat pleno & evaluasi internal.
        - Berkoordinasi dengan Departemen/Divisi lain mengenai hal-hal terkait
        pendampingan internal.
        GRAND DESIGN
        BADAN PENGURUS HARIAN
        HIMA IF 2024
        E. Departemen Internal
        - Menaungi divisi KMS dan BNK.
        - Mengkoordinasikan dan menjaga stabilitas divisi-divisi yang dinaunginya.
        - Membuat grand design alur bergerak divisi yang dibawahi.
        - Mengawasi serta mengevaluasi jalannya program divisi-divisi yang dibawahi
        berdasarkan visi dan misi, AD/ART, nilai yang dijunjung, serta GBHO.
        - Bertanggung jawab kepada ketua dan wakil ketua himpunan informatika.
        - Memberikan saran/masukan/rekomendasi mengenai permasalahan yang
        dihadapi oleh divisi- divisi yang dinaungi.
        1. Div. Kemahasiswaan (KMS)
        ● Memberikan pelayanan dan pendampingan atas permasalahan yang
        dihadapi oleh mahasiswa S1 Informatika Telkom University.
        ● Membangun platform yang mewadahi mahasiswa S1 Informatika Telkom
        University demi meningkatkan tingkat keharmonisan HIMA IF.
        2. Div. Bisnis dan Kewirausahaan (BNK)
        ● Merancang serta menentukan rencana pendapatan HIMA IF Telkom
        University secara kreatif dan halal.
        ● Menumbuhkan potensi kewirausahaan mahasiswa S1 Informatika Telkom
        University.
        ● Melakukan pendataan mahasiswa S1 Informatika yang telah memiliki
        bisnis/wirausaha.
        ● Mewadahi mahasiswa S1 Informatika Telkom University untuk
        menyalurkan minat terhadap bidang kewirausahaan.
        F. Departemen Eksternal
        - Menaungi divisi RKS dan MIK.
        - Mengkoordinasikan dan menjaga stabilitas divisi-divisi yang dinaunginya.
        - Membuat grand design alur bergerak divisi yang dibawahi.
        - Mengawasi serta mengevaluasi jalannya program divisi-divisi yang dibawahi
        berdasarkan visi dan misi, AD/ART, nilai yang dijunjung, serta GBHO.
        - Bertanggung jawab kepada Ketua dan Wakil Ketua HIMA IF.
        - Memberikan Saran/masukan/rekomendasi mengenai permasalahan yang
        GRAND DESIGN
        BADAN PENGURUS HARIAN
        HIMA IF 2024
        dihadapi oleh divisi- divisi yang dinaungi.
        1. Div. Relasi Eksternal (RKS)
        ● Membangun hubungan yang harmonis dan ditunjang dengan komunikasi
        yang rutin terhadap seluruh himpunan dan ormawa di Telkom University.
        ● Menjalin dan menjaga relasi yang baik dengan seluruh Himpunan Mahasiswa
        S1 Informatika di Indonesia guna meningkatkan hubungan yang harmonis
        antar Himpunan Mahasiswa Informatika.
        ● Menjadi bank data alumni HIMA IF Telkom University, perusahaan, dan mitra
        strategis.
        ● Menjalin dan menjaga hubungan serta bekerjasama dengan mitra strategis,
        alumni, perusahaan, serta lembaga-lembaga di dalam maupun di luar HIMA
        IF Telkom University yang berbasis profit.
        ● Meningkatkan nama baik HIMA IF di forum-forum komunikasi.
        ● Membentuk citra HIMA IF di mata pihak eksternal.
        2. Div. Media, Informasi, dan Komunikasi (MIK)
        ● Membuat SOP distribusi informasi secara struktural dan efisien.
        ● Mengelola media BPH HIMA IF Telkom University.
        ● Memenuhi kebutuhan desain dan konten kreatif yang menunjang media HIMA
        IF sesuai kebutuhan.
        ● Sebagai distributor informasi bagi mahasiswa S1 Informatika Telkom
        University.
        ● Melakukan dokumentasi kerja BPH HIMA IF Telkom University.
        G. Departemen Pengembangan Sumber Daya Mahasiswa
        - Menaungi divisi KDR, MNB, dan ARK.
        - Mengkoordinasikan dan menjaga stabilitas divisi-divisi yang dinaunginya.
        - Membuat grand design alur bergerak divisi yang dibawahi.
        - Mengawasi serta mengevaluasi jalannya program divisi-divisi yang dibawahi
        berdasarkan visi dan misi, AD/ART, nilai yang dijunjung, serta GBHO.
        - Bertanggung jawab kepada Ketua dan Wakil Ketua HIMA IF.
        - Memberikan saran/masukan/rekomendasi mengenai permasalahan yang
        dihadapi oleh divisi- divisi yang dinaungi.
        GRAND DESIGN
        BADAN PENGURUS HARIAN
        HIMA IF 2024
        1. Div. Kaderisasi (KDR)
        ● Merencanakan, menyusun strategi, dan mengaplikasikan sistem pengkaderan
        yang komprehensif dan stabil agar terciptanya kader-kader HIMA IF yang
        diharapkan.
        ● Melakukan program kerja edukasi pemahaman organisasi terhadap staf
        muda BPH HIMA IF.
        2. Div. Minat dan Bakat (MNB)
        ● Mengkolaborasikan pihak-pihak komunitas yang ada di jurusan S1
        Informatika sehingga dapat mengeksplorasi minat dan bakat mahasiswa S1
        Informatika Telkom University.
        ● Menjaring minat dan bakat HIMA IF dalam bidang kesenian dan olahraga.
        ● membina minat dan bakat HIMA IF melalui program kerja yang dibuat.
        ● Mengakomodir kebutuhan untuk menyalurkan minat dan bakat yang dimiliki
        mahasiswa S1 Informatika.
        3. Div. Akademik, Riset, dan Keprofesian (ARK)
        ● Melakukan program kerja yang berkaitan dengan membangun dan
        meningkatkan prestasi HIMA IF Telkom University.
        ● Mewadahi dan memfasilitasi kebutuhan dan keperluan akademik HIMA IF
        Telkom University.
        ● Merekap data prestasi mahasiswa S1 Informatika di bidang akademik.
        ● Meningkatkan budaya riset ilmiah dengan media kreatif di kalangan mahasiswa
        S1 Informatika Telkom University.
        ● Bekerjasama dengan instansi akademik terkait untuk menghasilkan karya yang
        aplikatif.
        ● Mengawal pelayanan mahasiswa utamanya dalam hal pendanaan bagi
        mahasiswa yang ikut kompetisi ilmiah.
        ● Melakukan pendampingan terhadap mahasiswa yang memiliki minat dalam
        kompetisi ilmiah.

        website resmi: https://himaiftelkom.com/
    
    Jawablah semua pertanyaan seputar kabinet ini dengan informasi langsung terkait struktur organisasi, program kerja, visi, misi, dan detail peran masing-masing departemen.
    """

    # vertexai.init(project=' your project name', location='asia-southeast1')
    model = GenerativeModel(
        'gemini-1.5-flash-001',
        system_instruction=[context]
    )

    return model.start_chat()
