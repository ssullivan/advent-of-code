package com.github.ssullivan.day18;

import java.io.IOException;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.LinkedBlockingQueue;

public class RunDuetPart2 {

  public static void main(String[] args) throws IOException, InterruptedException {
    final BlockingQueue<Long> program1MessageQueue = new LinkedBlockingQueue<>();
    final BlockingQueue<Long> program2MessageQueue = new LinkedBlockingQueue<>();


    final DuetProgramPart2 program1 = new DuetProgramPart2(0, program1MessageQueue, program2MessageQueue);
    final DuetProgramPart2 program2 = new DuetProgramPart2(1, program2MessageQueue, program1MessageQueue);

    Thread thread1 = runInThread(program1);
    Thread thread2 = runInThread(program2);

    thread1.start();
    thread2.start();

    CountDownLatch latch = new CountDownLatch(1);
    while (true) {
      int j = 0;
    }


  }

  private static Thread runInThread(final DuetProgramPart2 program) {
    return new Thread() {
      @Override
      public void run() {

        try {
          program.load(RunDuet.class.getClassLoader().getResourceAsStream("day18.txt"));
          program.run();
        } catch (IOException e) {
          e.printStackTrace();
        }
      }
    };
  }

}
