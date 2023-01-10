package homework6;

import java.util.HashSet;
import java.util.Set;

public class job3 {
    public static void main(String[] args) {
// Создание объектов класса job2
        job2 hp_pailion_g6 = new job2("hp_pailion_g6", 16, "4k", 
        true, 500, "16", "Windows", "black"); 
        job1 brandHp = new job1("HP", "U.S.A.", "AmericaLanguage");
        hp_pailion_g6.addBrand(brandHp); 
        job2 hp_galaxy_x64 = new job2("hp_galaxy_x64", 14, "FullHD", 
        true, 500, "8", "Windows", "white");
        hp_galaxy_x64.addBrand(brandHp);
        job2 samsung_a52 = new job2("samsung_a52", 18, "FullHD", 
        true, 300, "8", "Windows", "black");
        job1 brandSamsung = new job1("Samsung", "Korea", "KoreaLanguage");
        samsung_a52.addBrand(brandSamsung);
        job2 samsung_m31s = new job2("samsung_m31s", 16, "4k", 
        false, 1000, "16", "Linux", "black");
        samsung_m31s.addBrand(brandSamsung);
        job2 lenovo_gtx76 = new job2("lenovo_gtx76", 16, "FullHD", 
        true, 700, "8", "Windows", "white");
        job1 brandLenovo = new job1("Lenovo", "China", "ChinaLanguage");
        lenovo_gtx76.addBrand(brandLenovo);
        job2 macbook_14pro = new job2("macbook_14pro", 17, "4k", 
        false, 1000, "8", "ios", "white");
        job1 brandMacbook = new job1("Apple", "U.S.A.", "AmericaLanguage");
        macbook_14pro.addBrand(brandMacbook);
        job2 asus_x515 = new job2("asus_x515", 17, "FullHD", 
        true, 300, "4", "Windows", "black");
        job1 brandAsus = new job1("Asus", "taiwan", "ChinaLanguage");
        asus_x515.addBrand(brandAsus);
        job2 acer_air5 = new job2("acer_air5", 19, "FullHD", 
        true, 600, "8", "Windows", "black");
        job1 brandAcer = new job1("Acer", "taiwan", "ChinaLanguage");
        acer_air5.addBrand(brandAcer);
        job2 acer_air6 = new job2("acer_air6" ,18, "4k", 
        false, 500, "16", "Windows", "black");
        acer_air6.addBrand(brandAcer);
        job2 acer_a313 = new job2("acer_a313", 16, "FullHD", 
        true, 500, "8", "Windows", "black");
        acer_a313.addBrand(brandAcer);
// Создание множества
        Set <job2> laptop = new HashSet<>();
        laptop.add(hp_pailion_g6);      
        laptop.add(hp_galaxy_x64);
        laptop.add(samsung_a52);
        laptop.add(samsung_m31s);
        laptop.add(lenovo_gtx76);
        laptop.add(macbook_14pro);
        laptop.add(asus_x515);
        laptop.add(acer_air5);
        laptop.add(acer_air6);
        laptop.add(acer_a313);
// создание нового объекта вызова методов
        job2 FilterLaptop = new job2();
// вызов метода фильтрации по определеннеым параметрам
        // System.out.println("по вашему запросу найдено: " + FilterLaptop.filter(laptop));

// вызод метода фильтрации по заданным пользователем критериям
        System.out.println(FilterLaptop.newFilter(laptop));
    }
}