package com.clmas.collector;

import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;
import java.time.LocalDateTime;

public class LogCollector {

    public static void main(String[] args) throws Exception {
        while (true) {
            String json = String.format("{\"level\":\"INFO\",\"message\":\"Java agent log\",\"source\":\"java-agent\",\"timestamp\":\"%s\"}", LocalDateTime.now());
            sendLog(json);
            Thread.sleep(10000);
        }
    }

    public static void sendLog(String json) throws Exception {
        URL url = new URL("http://localhost:8080/logs");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setDoOutput(true);

        try (OutputStream os = conn.getOutputStream()) {
            os.write(json.getBytes());
            os.flush();
        }
        System.out.println("Sent log: " + conn.getResponseCode());
        conn.disconnect();
    }
}
