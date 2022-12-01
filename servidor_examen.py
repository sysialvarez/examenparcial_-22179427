{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5967b371-5932-4021-9af8-6a7d0f96ae96",
   "metadata": {},
   "outputs": [],
   "source": [
    "import socket, threading, sys, pickle, os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e8a9ae8-fe04-43b6-b299-56c273e78990",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Servidor():\n",
    "\n",
    "\tdef __init__(self, host=socket.gethostname(), port=int(input(\"Que puerto quiere usar ? \"))):\n",
    "\t\tself.clientes = []\n",
    "\t\tself.hostname = []\n",
    "\t\tprint('\\nSu IP actual es : ',socket.gethostbyname(host))\n",
    "\t\tprint('\\n\\tProceso con PID = ',os.getpid(), '\\n\\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\\n\\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(), '\\n\\tTotal Hilos activos en este punto del programa =', threading.active_count())\n",
    "\t\tself.s = socket.socket()\n",
    "\t\tself.s.bind((str(host), int(port)))\n",
    "\t\tself.s.listen(30)\n",
    "\t\tself.s.setblocking(False)\n",
    "\n",
    "\t\tthreading.Thread(target=self.aceptarC, daemon=True).start()\n",
    "\t\tthreading.Thread(target=self.procesarC, daemon=True).start()\n",
    "\n",
    "\t\twhile True:\n",
    "\t\t\tmsg = input('\\n << SALIR = 1 >> \\n')\n",
    "\t\t\tif msg == '1':\n",
    "\t\t\t\tprint(\" **** Me piro vampiro; cierro socket y mato SERVER con PID = \", os.getpid())\n",
    "\t\t\t\tself.s.close()\n",
    "\t\t\t\tsys.exit()\n",
    "\t\t\telse: pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9a03fdf-bfd0-4899-acf9-db71f69149df",
   "metadata": {},
   "outputs": [],
   "source": [
    "def aceptarC(self):\n",
    "\t\tprint('\\nHilo ACEPTAR con ID =',threading.currentThread().getName(), '\\n\\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\\n\\tPertenece al PROCESO con PID', os.getpid(), \"\\n\\tHilos activos TOTALES \", threading.active_count())\n",
    "\t\t\n",
    "\t\twhile True:\n",
    "\t\t\ttry:\n",
    "\t\t\t\tconn, addr = self.s.accept()\n",
    "\t\t\t\tprint(f\"\\nConexion aceptada via {addr}\\n\")\n",
    "\t\t\t\tconn.setblocking(False)\n",
    "\t\t\t\tself.clientes.append(conn)\n",
    "\t\t\t\tdata = conn.recv(32).decode()\n",
    "\t\t\t\tif data:\n",
    "\t\t\t\t\thostname = data\n",
    "\t\t\t\t\tprint(\"Hostname conectado: \", hostname)\n",
    "\t\t\t\t\tself.hostname.append(hostname)\n",
    "\t\t\texcept: pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d013020-1b18-4bf9-a048-ef65d9cb4481",
   "metadata": {},
   "outputs": [],
   "source": [
    "def procesarC(self):\n",
    "\t\tprint('\\nHilo PROCESAR con ID =',threading.currentThread().getName(), '\\n\\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\\n\\tPertenece al PROCESO con PID', os.getpid(), \"\\n\\tHilos activos TOTALES \", threading.active_count())\n",
    "\t\twhile True:\n",
    "\t\t\tif len(self.clientes) > 0:\n",
    "\t\t\t\tfor c in self.clientes:\n",
    "\t\t\t\t\ttry:\n",
    "\t\t\t\t\t\tdata = c.recv(32)\n",
    "\t\t\t\t\t\tif data: self.broadcast(data,c)\n",
    "\t\t\t\t\t\twith open('u22179427AI1.txt', 'a') as f:\n",
    "\t\t\t\t\t\t\tf.write(pickle.loads(data) + '\\n')\n",
    "\t\t\t\t\texcept: pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60d791e2-d313-4b0b-83e0-4122e33e946a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def broadcast(self, msg, cliente):\n",
    "\t\tfor c in self.clientes:\n",
    "\t\t\tprint(\"Clientes conectados Right now = \", len(self.clientes), ' ', self.hostname, '\\t El mensaje es de: ', pickle.loads(msg))\n",
    "\t\t\ttry:\n",
    "\t\t\t\tif c != cliente: \n",
    "\t\t\t\t\tprint(pickle.loads(msg))\n",
    "\t\t\t\t\tc.send(msg)\n",
    "\t\t\texcept: self.clientes.remove(c)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c64c708-dc81-497d-ab65-496727d96f88",
   "metadata": {},
   "outputs": [],
   "source": [
    "arrancar = Servidor() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad312602-9e30-43f1-9e4f-9ca2b661cc15",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
