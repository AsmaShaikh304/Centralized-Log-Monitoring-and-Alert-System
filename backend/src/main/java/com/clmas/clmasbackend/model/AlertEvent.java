package com.clmas.clmasbackend.model;

import jakarta.persistence.*;

@Entity
public class AlertEvent {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String logMessage;      // log that triggered the alert
    private String ruleName;        // name of the rule matched
    private String triggeredAt;     // timestamp

    public AlertEvent() {}

    // --- Getters and Setters ---

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getLogMessage() {
        return logMessage;
    }

    public void setLogMessage(String logMessage) {
        this.logMessage = logMessage;
    }

    public String getRuleName() {
        return ruleName;
    }

    public void setRuleName(String ruleName) {
        this.ruleName = ruleName;
    }

    public String getTriggeredAt() {
        return triggeredAt;
    }

    public void setTriggeredAt(String triggeredAt) {
        this.triggeredAt = triggeredAt;
    }
}
