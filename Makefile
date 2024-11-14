# Makefile

# Variables para los nombres de los archivos
DB_FILE = db.sqlite3
OLD_DB_FILE = db_anterior.sqlite3
BASE_DB_FILE = db_test_base.sqlite3

# Target principal
.PHONY: reset-db clean-db
start-db: rename-db copy-db
clean-db: delete-db restore-old-db

# Cambiar el nombre del archivo bd.sqlite3 a bd_anterior.sqlite3
rename-db:
	@if [ -f $(DB_FILE) ]; then \
		mv $(DB_FILE) $(OLD_DB_FILE); \
		echo "Renombrado $(DB_FILE) a $(OLD_DB_FILE)"; \
	else \
		echo "$(DB_FILE) no existe. No se renombrará."; \
	fi

# Copiar bd_test_base.sqlite3 a bd.sqlite3
copy-db:
	@if [ -f $(BASE_DB_FILE) ]; then \
		cp $(BASE_DB_FILE) $(DB_FILE); \
		echo "Copiado $(BASE_DB_FILE) a $(DB_FILE)"; \
	else \
		echo "$(BASE_DB_FILE) no existe. No se puede copiar."; \
	fi

# Limpiar ambiente de pruebas - Borrar bd.sqlite3 y restaurar bd_anterior.sqlite3 a bd.sqlite3
delete-db:
	@if [ -f $(DB_FILE) ]; then \
		rm $(DB_FILE); \
		echo "$(DB_FILE) borrado."; \
	else \
		echo "$(DB_FILE) no existe. No hay nada que borrar."; \
	fi

# Restaurar bd_anterior.sqlite3 como bd.sqlite3
restore-old-db:
	@if [ -f $(OLD_DB_FILE) ]; then \
		mv $(OLD_DB_FILE) $(DB_FILE); \
		echo "Restaurado $(OLD_DB_FILE) a $(DB_FILE)"; \
	else \
		echo "$(OLD_DB_FILE) no existe. No se puede restaurar."; \
	fi
