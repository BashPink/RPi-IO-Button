#! /bin/sh

### BEGIN INIT INFO
# Provides:          Spyglass_PC.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

case "$1" in
  start)
    echo "Starting Listener"
    /usr/local/bin/Spyglass_PC.py &
    ;;
  stop)
    echo "Stopping Listener"
    pkill -f /usr/local/bin/Spyglass_PC.py
    ;;
  *)
    echo "Usage: /etc/init.d/Spyglass_PC.sh"
    exit 1
    ;;
esac

exit 0
