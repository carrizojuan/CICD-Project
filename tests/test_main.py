def test_hello_world(capsys):
    # Importa tu módulo principal
    from src import main

    # Ejecuta tu código principal
    main.main()

    # Captura la salida del print
    captured = capsys.readouterr()

    # Comprueba si la salida coincide con el mensaje esperado
    assert captured.out.strip() == "Hola Mundo"