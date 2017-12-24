package com.github.ssullivan.day18;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;
import java.util.regex.Pattern;

public class DuetProgram {
  private static final Pattern IS_ALPHA = Pattern.compile("^[a-zA-Z]$");
  private static final Pattern IS_INT = Pattern.compile("^-?[0-9]+$");
  private List<Instruction> instructions;
  private Long _sounds;
  private Map<String, Long> registers = new HashMap<>();
  private Integer offset;

  public DuetProgram() {
  }

  public void load(final InputStream inputStream) throws IOException {
    this.instructions = new ArrayList<>();
    this.offset = 0;

    try (final BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream))) {
      String line = null;

      while ((line = bufferedReader.readLine()) != null) {
        if (line.isEmpty())
          continue;

        final Instruction instruction = new Instruction(line);
        this.instructions.add(instruction);

      }
    }
  }

  public void run() {
    final int maxOffset = this.instructions.size();

    while (offset >= 0 || offset < maxOffset) {
      final Instruction instruction = this.instructions.get(offset);

      switch (instruction.getInstruction()) {
        case "snd":
          snd(instruction.getX());
          break;
        case "set":
          set(instruction.getX(), instruction.getY());
          break;
        case "add":
          add(instruction.getX(), instruction.getY());
          break;
        case "mul":
          mul(instruction.getX(), instruction.getY());
          break;
        case "mod":
          mod(instruction.getX(), instruction.getY());
          break;
        case "rcv":
          this.rcv(instruction.getX());
          break;
        case "jgz":
          this.jgz(instruction.getX(), instruction.getY());
          break;
        default:
          throw new InvalidInstruction();
      }

      if (! "jgz".equalsIgnoreCase(instruction.getInstruction()))
        offset += 1;
      int k = 0;
    }
  }

  private long get(final String registerOrValue) {
    if (isAlpha(registerOrValue)) {
      // its a register, so retrieve the value
      return this.registers.getOrDefault(registerOrValue, 0L);
    }
    else if (isInt(registerOrValue)) {
      return Integer.parseInt(registerOrValue, 10);
    }

    return 0;
  }

  private boolean isInt(final String s) {
    return s != null && IS_INT.matcher(s).matches();
  }

  private boolean isAlpha(final String s) {
    return null != s && IS_ALPHA.matcher(s).matches();
  }


  private void set(final String x, final String y) {
    this.registers.put(x, get(y));
  }

  private void mul(final String x, final String y) {
    this.registers.put(x, get(x) * get(y));
  }

  private void add(final String x, final String y) {
    this.registers.put(x, get(x) + get(y));
  }

  private void mod(final String x, final String y) {
    this.registers.put(x, get(x) % get(y));
  }

  private void snd(final String x) {
    _sounds = get(x);
  }

  private void rcv(final String x) {
    if (get(x) != 0)
      System.out.println("Part 1: " + _sounds);
  }

  private void jgz(final String x, final String y) {
    if (get(x) > 0) {
      offset += (int) get(y);
    }
    else {
      offset++;
    }
  }
}
