package com.clmas.clmasbackend.service;

import com.clmas.clmasbackend.model.LogEntry;
import com.clmas.clmasbackend.repository.LogRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class LogQueryService {

    @Autowired
    private LogRepository logRepository;

    public List<LogEntry> getAllLogs() {
        return logRepository.findAll();
    }

    public LogEntry saveLog(LogEntry log) {
        return logRepository.save(log);
    }
}
