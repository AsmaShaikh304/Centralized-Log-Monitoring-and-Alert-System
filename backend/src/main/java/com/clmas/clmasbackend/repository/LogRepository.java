package com.clmas.clmasbackend.repository;

import com.clmas.clmasbackend.model.LogEntry;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LogRepository extends JpaRepository<LogEntry, Long> {}
