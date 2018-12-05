package com.github.ssullivan.day18;

import java.io.IOException;

public class RunDuet {

  public static void main(String[] args) throws IOException {
    DuetProgram duetProgram = new DuetProgram();

    duetProgram.load(RunDuet.class.getClassLoader().getResourceAsStream("day18.txt"));
    duetProgram.run();
    int j = 0;

  }
}
