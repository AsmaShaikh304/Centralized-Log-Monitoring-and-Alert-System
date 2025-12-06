package com.clmas.clmasbackend.controller;

import com.clmas.clmasbackend.model.AlertRule;
import com.clmas.clmasbackend.repository.AlertRuleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/alertRules")
public class AlertRuleController {

    @Autowired
    private AlertRuleRepository alertRuleRepository;

    // CREATE
    @PostMapping
    public AlertRule createRule(@RequestBody AlertRule alertRule) {
        return alertRuleRepository.save(alertRule);
    }

    // GET ALL
    @GetMapping
    public List<AlertRule> getAllRules() {
        return alertRuleRepository.findAll();
    }

    // GET BY ID
    @GetMapping("/{id}")
    public AlertRule getRuleById(@PathVariable Long id) {
        return alertRuleRepository.findById(id).orElse(null);
    }

    // UPDATE
    @PutMapping("/{id}")
    public AlertRule updateRule(
            @PathVariable Long id,
            @RequestBody AlertRule updatedRule) {

        AlertRule rule = alertRuleRepository.findById(id).orElse(null);
        if (rule == null) return null;

        rule.setName(updatedRule.getName());
        rule.setCondition(updatedRule.getCondition());
        return alertRuleRepository.save(rule);
    }

    // DELETE
    @DeleteMapping("/{id}")
    public String deleteRule(@PathVariable Long id) {
        alertRuleRepository.deleteById(id);
        return "Deleted";
    }
}
