package com.layer10.tollfeecalculator.models;

import java.time.LocalDateTime;

public class Passage {
    private String vehicle;
    private LocalDateTime dateTime;

    public Passage() {}

    public Passage(String vehicle, LocalDateTime dateTime) {
        this.vehicle = vehicle;
        this.dateTime = dateTime;
    }

    public String getVehicle() {
        return vehicle;
    }

    public void setVehicle(String vehicle) {
        this.vehicle = vehicle;
    }

    public LocalDateTime getDateTime() {
        return dateTime;
    }

    public void setDateTime(LocalDateTime dateTime) {
        this.dateTime = dateTime;
    }
}