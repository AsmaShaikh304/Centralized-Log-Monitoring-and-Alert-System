package com.clmas.clmasbackend.repository;

import com.clmas.clmasbackend.model.AlertRule;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AlertRuleRepository extends JpaRepository<AlertRule, Long> {}
