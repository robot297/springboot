package connections;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Accounts {
    public String getUsers() {

        StringBuffer response = new StringBuffer();
        int status;

        try {
            URL url = new URL("https://alpha-api.usbank.com/innovations/v1/users");
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
