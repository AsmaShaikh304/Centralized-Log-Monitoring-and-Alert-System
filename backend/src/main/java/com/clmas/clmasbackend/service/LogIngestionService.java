package com.clmas.clmasbackend.service;

import com.clmas.clmasbackend.model.LogEntry;
import com.clmas.clmasbackend.repository.LogRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LogIngestionService {

    @Autowired
    private LogRepository logRepository;

    public LogEntry ingestLog(LogEntry log) {
        return logRepository.save(log);
    }
}
