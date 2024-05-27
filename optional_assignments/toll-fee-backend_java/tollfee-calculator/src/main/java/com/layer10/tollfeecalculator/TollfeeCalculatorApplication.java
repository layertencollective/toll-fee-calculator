package com.layer10.tollfeecalculator;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Info;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@OpenAPIDefinition(info = @Info(title = "Toll Fee Calculator API", version = "1.0", description = "API for calculating toll fees"))
public class TollfeeCalculatorApplication {

	public static void main(String[] args) {
		SpringApplication.run(TollfeeCalculatorApplication.class, args);
	}

}
