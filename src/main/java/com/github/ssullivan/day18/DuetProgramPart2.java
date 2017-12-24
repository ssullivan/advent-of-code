package com.github.ssullivan.day18;

import java.util.concurrent.BlockingQueue;

public class DuetProgramPart2 extends DuetProgram {
  private int id;
  private BlockingQueue<Long> inputQueue;
  private BlockingQueue<Long> outputQueue;
  private Long counter = 0L;

  public DuetProgramPart2(int id,
      BlockingQueue<Long> inputQueue,
      BlockingQueue<Long> outputQueue) {
    this.id = id;
    this.inputQueue = inputQueue;
    this.outputQueue = outputQueue;

    set("p", (long) id);
  }

  public Long getCounter() {
    return counter;
  }

  @Override
  protected void snd(String x) {
   if (this.outputQueue.offer(get(x))) {
     this.counter++;
   }
  }

  @Override
  protected void rcv(String x) throws InterruptedException {
    if (id == 1)
      System.out.println("Part 2 [id: " + id + "] " + this.counter);
   set(x, this.inputQueue.take());
  }
}
