package com.github.ssullivan.day18;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class DuetProgram {
  private List<Instruction> instructions;
  private Stack<Integer> sounds;
  private Registers registers;
  private Integer offset;

  public DuetProgram() {
  }

  public void load(final InputStream inputStream) throws IOException {
    this.instructions = new ArrayList<>();
    this.sounds = new Stack<>();
    this.registers = new Registers();
    this.offset = 0;

    try (final BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream))) {
      String line = null;

      while ((line = bufferedReader.readLine()) != null) {
        if (line.isEmpty())
          continue;

        this.instructions.add(new Instruction(line));
      }
    }
  }

  public void run() {
    while (true) {
      final Instruction instruction = this.instructions.get(offset);

      switch (instruction.getInstruction()) {
        case "snd":
          break;
        case "set":
          break;
        case "add":
          break;
        case "mul":
          break;
        case "mod":
          break;
        case "rcv":
          break;
        case "jgz":
          break;
        default:
          throw new InvalidInstruction();
      }
    }
  }
}
