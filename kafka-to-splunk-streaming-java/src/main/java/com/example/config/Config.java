package com.example.config;

public class Config {
    public static final String KAFKA_BOOTSTRAP_SERVERS = System.getenv().getOrDefault("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092");
    public static final String KAFKA_TOPIC = System.getenv().getOrDefault("KAFKA_TOPIC", "infra-metrics");
    public static final String SPLUNK_HEC_URL = System.getenv().getOrDefault("SPLUNK_HEC_URL", "http://localhost:8088");
    public static final String SPLUNK_TOKEN = System.getenv().getOrDefault("SPLUNK_TOKEN", "");
    public static final String DEFAULT_SPLUNK_INDEX = System.getenv().getOrDefault("SPLUNK_INDEX", "main");
    public static final String CUSTOM_TEXT = System.getenv().getOrDefault("CUSTOM_TEXT", "_logs");

}
