{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "50d6fa63-9961-49ba-b6f6-908a491d9ccc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import threading, sys, socket, pickle, os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bc3beea2-3b44-407f-a662-080eae81930e",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [2], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mCliente\u001b[39;00m():\n\u001b[1;32m      3\u001b[0m \t\u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__init__\u001b[39m(\u001b[38;5;28mself\u001b[39m, hostname\u001b[38;5;241m=\u001b[39m\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIntroduzca el hostname de su cliente: \u001b[39m\u001b[38;5;124m\"\u001b[39m), host\u001b[38;5;241m=\u001b[39m\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIntoduzca la IP del servidor ?  \u001b[39m\u001b[38;5;124m\"\u001b[39m), port\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIntoduzca el PUERTO del servidor ?  \u001b[39m\u001b[38;5;124m\"\u001b[39m))):\n\u001b[1;32m      4\u001b[0m \t\t\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39ms \u001b[38;5;241m=\u001b[39m socket\u001b[38;5;241m.\u001b[39msocket()\n",
      "Cell \u001b[0;32mIn [2], line 3\u001b[0m, in \u001b[0;36mCliente\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mCliente\u001b[39;00m():\n\u001b[0;32m----> 3\u001b[0m \t\u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__init__\u001b[39m(\u001b[38;5;28mself\u001b[39m, hostname\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mIntroduzca el hostname de su cliente: \u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m, host\u001b[38;5;241m=\u001b[39m\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIntoduzca la IP del servidor ?  \u001b[39m\u001b[38;5;124m\"\u001b[39m), port\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIntoduzca el PUERTO del servidor ?  \u001b[39m\u001b[38;5;124m\"\u001b[39m))):\n\u001b[1;32m      4\u001b[0m \t\t\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39ms \u001b[38;5;241m=\u001b[39m socket\u001b[38;5;241m.\u001b[39msocket()\n\u001b[1;32m      5\u001b[0m \t\t\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39ms\u001b[38;5;241m.\u001b[39mconnect((host, \u001b[38;5;28mint\u001b[39m(port)))\n",
      "File \u001b[0;32m/opt/homebrew/lib/python3.10/site-packages/ipykernel/kernelbase.py:1177\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1173\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_allow_stdin:\n\u001b[1;32m   1174\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(\n\u001b[1;32m   1175\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m   1176\u001b[0m     )\n\u001b[0;32m-> 1177\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_input_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   1178\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mprompt\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1179\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent_ident\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1180\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_parent\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1181\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpassword\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[1;32m   1182\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m/opt/homebrew/lib/python3.10/site-packages/ipykernel/kernelbase.py:1219\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1216\u001b[0m             \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[1;32m   1217\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[1;32m   1218\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[0;32m-> 1219\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28mNone\u001b[39m\n\u001b[1;32m   1220\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[1;32m   1221\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "class Cliente():\n",
    "\n",
    "\tdef __init__(self, hostname=input(\"Introduzca el hostname de su cliente: \"), host=input(\"Intoduzca la IP del servidor ?  \"), port=int(input(\"Intoduzca el PUERTO del servidor ?  \"))):\n",
    "\t\tself.s = socket.socket()\n",
    "\t\tself.s.connect((host, int(port)))\n",
    "\t\tself.hostname=hostname\n",
    "\t\tself.s.send(hostname.encode())\n",
    "\t\tprint('\\n\\tProceso con PID = ',os.getpid(), '\\n\\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\\n\\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\\n\\tTotal Hilos activos en este punto del programa =', threading.active_count())\n",
    "\t\tthreading.Thread(target=self.recibir, daemon=True).start()\n",
    "\n",
    "\t\twhile True:\n",
    "\t\t\tmsg = input('\\nHostname: ' + self.hostname + '\\nEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1 \\n')\n",
    "\t\t\tif msg != '1' : self.enviar(msg)\n",
    "\t\t\telse:\n",
    "\t\t\t\tprint(\" **** Me piro vampiro; cierro socket y mato al CLIENTE con PID = \", os.getpid())\n",
    "\t\t\t\tself.s.close()\n",
    "\t\t\t\tsys.exit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "770ee8de-6f7d-4043-86ac-bf9a8ec25608",
   "metadata": {},
   "outputs": [],
   "source": [
    "def recibir(self):\n",
    "\t\tprint('\\nHilo RECIBIR con ID =',threading.currentThread().getName(), '\\n\\tPertenece al PROCESO con PID', os.getpid(), \"\\n\\tHilos activos TOTALES \", threading.active_count())\n",
    "\t\twhile True:\n",
    "\t\t\ttry:\n",
    "\t\t\t\tdata = self.s.recv(32)\n",
    "\t\t\t\tif data: print(pickle.loads(data))\n",
    "\t\t\texcept: pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c5a245c-dee6-46ed-b8d4-1af6229970ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "def enviar(self, msg):\n",
    "\t\tmensaje = f\"{self.hostname}: {msg}\"\n",
    "\t\tself.s.send(pickle.dumps(mensaje))\n",
    "\n",
    "arrancar = Cliente()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58f83a5a-e3d1-4c28-948e-6041c73d7e81",
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
