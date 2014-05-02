import pythoncom
import win32serviceutil
import win32service
import win32event
import servicemanager

import httplib
# https://docs.python.org/2/library/httplib.html



class Pulsador:
    def __init__(self):
        pass

    def read(self):
        pass

    def write(self):
        pass


class ControlServer:
    server = "192.168.100.2"
    port = 80

    def __init__(self):
        pass


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"
    _svc_description_ = "Test Service description"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

    def main(self):
        control_server = ControlServer()

        # Loop:
        # - Read and write from control server
        # - Read and write to serial port


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)