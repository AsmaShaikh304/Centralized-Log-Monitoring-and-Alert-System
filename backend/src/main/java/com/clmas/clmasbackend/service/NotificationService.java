package com.clmas.clmasbackend.service;

import com.clmas.clmasbackend.model.AlertEvent;
import org.springframework.stereotype.Service;

@Service
public class NotificationService {

    public void sendNotification(AlertEvent event) {
        // Implement email/SMS/webhook logic here
        System.out.println("Alert triggered: " + event);
    }
}
