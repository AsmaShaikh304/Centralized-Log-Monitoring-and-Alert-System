package com.clmas.clmasbackend.controller;

import com.clmas.clmasbackend.model.AlertEvent;
import com.clmas.clmasbackend.repository.AlertEventRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/alertEvents")
public class AlertEventController {

    @Autowired
    private AlertEventRepository alertEventRepository;

    // Get all alert events
    @GetMapping
    public List<AlertEvent> getAllAlertEvents() {
        return alertEventRepository.findAll();
    }
}
