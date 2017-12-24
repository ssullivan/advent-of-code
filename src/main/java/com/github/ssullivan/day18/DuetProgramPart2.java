package com.github.ssullivan.day18;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class DuetProgramPart2 extends DuetProgram {

  private BlockingQueue<Long> inputQueue;
  private BlockingQueue<Long> outputQueue;

  public DuetProgramPart2(final BlockingQueue<Long> outputQueue) {
    this.inputQueue = new LinkedBlockingQueue<>();
    this.outputQueue = outputQueue;
  }

  @Override
  protected void snd(String x) {
    this.outputQueue.offer(get(x));
  }

  @Override
  protected void rcv(String x) throws InterruptedException {
   set(x, this.inputQueue.take());
  }
}
