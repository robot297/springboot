import connections.*;

public class Application {
    public static void main(String[] args) {

        Accounts accounts = new Accounts();
        Rates rates = new Rates();

        System.out.println(accounts.getUsers());
        System.out.println(rates.getAutoLoanRates());
    }
}