package com.clmas.clmasbackend.repository;

import com.clmas.clmasbackend.model.AlertEvent;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AlertEventRepository extends JpaRepository<AlertEvent, Long> {
}
