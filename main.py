from Usuario import Usuario

adrien = Usuario ("Adrien")
nibbles =Usuario ("Mr Nibbles")
bennyBob =Usuario ("Benny Bob")

adrien.hacer_deposito (100).hacer_deposito(150).hacer_deposito(100).hacer_retiro(45).mostrar_balance_usuario()




nibbles.hacer_deposito (1500).hacer_deposito(1000).hacer_retiro(500).hacer_retiro(800).mostrar_balance_usuario()



bennyBob.hacer_deposito(1000).hacer_retiro(1000).hacer_retiro(3000).hacer_retiro(4500).mostrar_balance_usuario()



adrien.hacerTransferencia(100, bennyBob)