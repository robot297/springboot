package Connections;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Rates {

    public String getAutoLoanRates() {
        StringBuffer response = new StringBuffer();
        String loanRate = "GetAutoLoanRates?application=RIB&output=json&branchnumber=1&zipcode=80130&regionid=1&loanamount=24000&loantermmonths=12&loanproduct=NEW";

        int status;

        try {
            URL url = new URL("https://alpha-api.usbank.com/innovation-rate/v1/" + loanRate);
            HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
            httpURLConnection.setRequestProperty("apiKey", "6uGda4NfwusAwTuRHMTdGaU5kBlQprmd");
            httpURLConnection.setRequestMethod("GET");

            status = httpURLConnection.getResponseCode();
            System.out.println(status);

            BufferedReader in = new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));

            String inputLine;


            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }

            httpURLConnection.disconnect();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        return response.toString();
    }
}
