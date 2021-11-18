#! /bin/sh

### BEGIN INIT INFO
# Provides:          scriptname
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

case "$1" in
  start)
    echo "Starting Listener"
    /usr/local/bin/shutdown-listener.py &
    ;;
  stop)
    echo "Stopping Listener"
    pkill -f /usr/local/bin/shutdown-listener.py
    ;;
  *)
    echo "Usage: /etc/init.d/shutdown-listener.sh
    exit 1
    ;;
esac

exit 0
