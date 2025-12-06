package com.clmas.clmasbackend.controller;

import com.clmas.clmasbackend.model.AlertEvent;
import com.clmas.clmasbackend.model.AlertRule;
import com.clmas.clmasbackend.model.LogEntry;
import com.clmas.clmasbackend.repository.AlertEventRepository;
import com.clmas.clmasbackend.repository.AlertRuleRepository;
import com.clmas.clmasbackend.repository.LogRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;

@RestController
@RequestMapping("/logs")
public class LogController {

    @Autowired
    private LogRepository logRepository;

    @Autowired
    private AlertRuleRepository alertRuleRepository;

    @Autowired
    private AlertEventRepository alertEventRepository;

    @PostMapping
    public LogEntry ingestLog(@RequestBody LogEntry log) {

        // STEP 1 — Save Log
        LogEntry savedLog = logRepository.save(log);

        // STEP 2 — Check Alert Rules
        for (AlertRule rule : alertRuleRepository.findAll()) {
            if (log.getMessage().contains(rule.getCondition())) {

                // STEP 3 — Create Alert Event
                AlertEvent alert = new AlertEvent();
                alert.setLogMessage(log.getMessage());
                alert.setRuleName(rule.getName());
                alert.setTriggeredAt(LocalDateTime.now().toString());

                alertEventRepository.save(alert);
            }
        }

        return savedLog;
    }
}
