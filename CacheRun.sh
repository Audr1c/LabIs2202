# !/bin/bash
sleep 10
telnet localhost 3456 &

sleep 30
./lud.riscv -s 256 -n 1
sleep 600