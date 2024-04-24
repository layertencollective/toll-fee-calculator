package com.layer10.tollfeecalculator.controllers;

import com.layer10.tollfeecalculator.models.Passage;
import com.layer10.tollfeecalculator.models.Vehicle;
import com.layer10.tollfeecalculator.services.TollFeeService;
import io.swagger.v3.oas.annotations.Operation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class TollFeeController {

    @Autowired
    private TollFeeService tollFeeService;

    @GetMapping("/ping")
    public ResponseEntity<String> ping() {
        return ResponseEntity.ok("pong");
    }

    @Operation(summary = "Get the toll fee for a specific vehicle and date/time")
    @GetMapping("/get-toll-fee")
    public ResponseEntity<Integer> getTollFee(@RequestParam String vehicle, @RequestParam String dateTime) {
        return ResponseEntity.ok(tollFeeService.calculateTollFee(vehicle, dateTime));
    }

    @Operation(summary = "Get all the toll fees for a specific vehicle from a list of dateTimes")
    @PostMapping("/get-all-fees-for-vehicle")
    public ResponseEntity<Integer> getAllFeesForVehicle(@RequestBody Vehicle vehicle) {
        return ResponseEntity.ok(tollFeeService.calculateAllFeesForVehicle(vehicle));
    }

    @Operation(summary = "Get all the toll fees for a list of passages")
    @PostMapping("/get-all-fees-for-list")
    public ResponseEntity<Integer> getAllFeesForList(@RequestBody List<Passage> passages) {
        return ResponseEntity.ok(tollFeeService.calculateAllFeesForList(passages));
    }
}