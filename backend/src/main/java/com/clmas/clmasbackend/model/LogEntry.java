package com.clmas.clmasbackend.model;

import jakarta.persistence.*;

@Entity
public class LogEntry {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String timestamp;
    private String level;
    
    @Column(columnDefinition = "TEXT")
    private String message;

    private String source;

    public Long getId() { return id; }
    public String getTimestamp() { return timestamp; }
    public String getLevel() { return level; }
    public String getMessage() { return message; }
    public String getSource() { return source; }

    public void setId(Long id) { this.id = id; }
    public void setTimestamp(String timestamp) { this.timestamp = timestamp; }
    public void setLevel(String level) { this.level = level; }
    public void setMessage(String message) { this.message = message; }
    public void setSource(String source) { this.source = source; }
}
