package homework6;

public class job1 {
    private String brand;
    private String country;
    private String language;

    public job1(String brand, String country, String language){
        this.brand = brand;
        this.country = country;
        this.language = language;
        }

    public String getBrand() {return brand;}
    public String getCountry() {return country;}
    public String getLanguage() {return language;}

    @Override
    public String toString() {
        return "Brand [brand= " + brand + ", country= " + country + ", language= " + language + "]";
    }
}
    
