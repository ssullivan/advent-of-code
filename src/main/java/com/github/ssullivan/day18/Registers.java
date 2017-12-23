package com.github.ssullivan.day18;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

public class Registers {
  private static final Pattern ALPHA = Pattern.compile("^[a-zA-Z]$");
  private Map<String, Integer> registers;

  public Registers() {
    this.registers = new HashMap<>();
  }

  public void set(final String register, final Integer value) {
    if (isValidRegister(register)) {
      throw new InvalidRegister();
    }

    this.registers.put(register, value);
  }

  public void add(final String register, final Integer value) {
    if (isValidRegister(register)) {
      throw new InvalidRegister();
    }

    this.registers.compute(register, (s, original) -> {
      if (original == null)
        return 0;
      return original + value;
    });
  }

  public void mul(final String register, final Integer value) {
    if (isValidRegister(register)) {
      throw new InvalidRegister();
    }

    this.registers.compute(register, (s, original) -> {
      if (original == null)
        return 0;
      return original * value;
    });
  }

  public void mod(final String register, final Integer value) {
    if (isValidRegister(register)) {
      throw new InvalidRegister();
    }

    this.registers.compute(register, (s, original) -> {
      if (original == null)
        return 0 % value;
      return original % value;
    });
  }

  private boolean isValidRegister(final String register) {
    return register != null && register.length() <= 1 && ALPHA.matcher(register).matches();
  }

}
