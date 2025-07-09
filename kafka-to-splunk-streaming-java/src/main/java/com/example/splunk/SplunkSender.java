package com.example.splunk;

import com.example.config.Config;
import org.json.JSONObject;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class SplunkSender {

    public static void sendToSplunk(String rawPayload) {
        try {
            JSONObject obj = new JSONObject(rawPayload);

String targetIndex;
if (obj.has("otel.splunkindex") && !obj.getString("otel.splunkindex").trim().isEmpty()) {
    String baseIndex = obj.getString("otel.splunkindex").trim();
    targetIndex = baseIndex + "_" + Config.CUSTOM_TEXT;

    // Optional: update the payload itself
    obj.put("otel.splunkindex", targetIndex);
} else {
    targetIndex = Config.DEFAULT_SPLUNK_INDEX;
}
            }

            JSONObject event = new JSONObject();
            event.put("event", obj);
            event.put("index", targetIndex);
            event.put("sourcetype", "_json");

            URL url = new URL(Config.SPLUNK_HEC_URL + "/services/collector/event");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Authorization", "Splunk " + Config.SPLUNK_TOKEN);
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            try (OutputStream os = conn.getOutputStream()) {
                os.write(event.toString().getBytes());
                os.flush();
            }

            int code = conn.getResponseCode();
            if (code != 200) {
                System.err.println("⚠️ Splunk HEC failed: " + code + " - " + conn.getResponseMessage());
            }

        } catch (Exception e) {
            System.err.println("🚨 Error sending to Splunk: " + e.getMessage());
        }
    }
}
