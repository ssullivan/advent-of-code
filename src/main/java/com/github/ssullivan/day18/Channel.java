package com.github.ssullivan.day18;

import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;

public class Channel {
  private Queue<Long> inputQueue;
  private Queue<Long> outputQueue;

  public Channel() {
    this.inputQueue = new LinkedBlockingQueue<>();
    this.outputQueue = new LinkedBlockingQueue<>();
  }
}
