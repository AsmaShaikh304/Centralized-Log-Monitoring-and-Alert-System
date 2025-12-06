package com.clmas.clmasbackend.service;

import com.clmas.clmasbackend.model.AlertRule;
import com.clmas.clmasbackend.repository.AlertRuleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AlertRuleService {

    @Autowired
    private AlertRuleRepository alertRuleRepository;

    public List<AlertRule> getAllRules() {
        return alertRuleRepository.findAll();
    }

    public AlertRule saveRule(AlertRule rule) {
        return alertRuleRepository.save(rule);
    }
}
