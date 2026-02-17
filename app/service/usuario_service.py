from fastapi import HTTPException
#from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config

def _table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.supabase_usuario)

def inicio(correo:str):
    try:
        res = _table().select("id_usuario, correo, contraseña, categaria").eq("correo", correo).execute()
        if res:
            return {"Usuario": res.data}
        else:
            raise HTTPException(status_code=404, detail="Error al encontrar el usuario")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar usuario {e}")