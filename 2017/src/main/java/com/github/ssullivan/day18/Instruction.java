package com.github.ssullivan.day18;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Instruction {

  private static final Pattern SND_PATTERN = Pattern.compile("^(snd) (-?\\d+|[a-zA-Z])$");
  private static final Pattern RCV_PATTERN = Pattern.compile("^(rcv) (-?\\d+|[a-zA-Z])$");
  private static final Pattern REGISTER_PATTERNS = Pattern.compile("^(set|add|mul|mod) ([a-zA-Z]) (-?\\d+|[a-zA-Z])$");
  private static final Pattern JUMP_PATTERN = Pattern.compile("^(jgz) (-?\\d+|[a-zA-Z]) (-?\\d+|[a-zA-Z])$");

  private String instruction;
  private String x;
  private String y;

  public Instruction(final String source) {

    Matcher matcher;

    if ((matcher = SND_PATTERN.matcher(source)).matches()) {
      this.instruction = matcher.group(1);
      this.x = matcher.group(2);

    }
    else if ((matcher = RCV_PATTERN.matcher(source)).matches()) {
      this.instruction = matcher.group(1);
      this.x = matcher.group(2);
    }
    else if ((matcher = REGISTER_PATTERNS.matcher(source)).matches()) {
      this.instruction = matcher.group(1);
      this.x =  matcher.group(2);
      this.y = matcher.group(3);
    }
    else if ((matcher = REGISTER_PATTERNS.matcher(source)).matches()) {
      this.instruction = matcher.group(1);
      this.x = matcher.group(2);
      this.y = matcher.group(3);
    }
    else if ((matcher = JUMP_PATTERN.matcher(source)).matches()) {
      this.instruction = matcher.group(1);
      this.x = matcher.group(2);
      this.y = matcher.group(3);
    }
    else {
      throw new InvalidInstruction();
    }
  }

  public String getInstruction() {
    return instruction;
  }

  public String getX() {
    return x;
  }

  public String getY() {
    return y;
  }

  @Override
  public String toString() {
    return "Instruction{" +
        "instruction='" + instruction + '\'' +
        ", x='" + x + '\'' +
        ", y='" + y + '\'' +
        '}';
  }
}
