from sqlalchemy import create_engine, MetaData, select, func, and_


DATABASE_URL = "postgresql://admin:udenstinti@10.3.7.131:8432/school_db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

tenant_entity_ids= [15802, 14113, 13448, 17650, 17652, 12657, 13408, 13393, 13478, 13465, 13440, 15357, 13479, 15918, 11985, 13417, 15801, 13462, 223, 16395, 12461, 13418, 60, 13439, 7959, 13416, 14643, 14120, 17493, 13394, 13446, 13419, 13444, 13450, 15289, 7917, 10941, 13426, 14289, 17209, 16967, 10432, 9448, 13461, 8758, 13458, 17843, 13421, 12, 13434, 16959, 14136, 17402, 13415, 10301, 17732, 16312, 15758, 13435, 9436, 13457, 16961, 13452, 13412, 9437, 13447, 15784, 14968, 17687, 13441, 9304]

identity = metadata.tables["identity"]
with engine.connect() as connection:
    query_identity = (
        select(
            identity.c.tenant_entity_id,
            func.count().label('user_count')
        )
        .where(and_(
            identity.c.is_active == True,  # Active users
            identity.c.photo.is_not(None),  # Has a photo
            identity.c.tenant_entity_id.in_(tenant_entity_ids)  # Filter to your list
        ))
        .group_by(identity.c.tenant_entity_id)
        .order_by(identity.c.tenant_entity_id)
    )

    result = connection.execute(query_identity)

    # Convert to dictionary {tenant_id: count}
    tenant_counts = {row.tenant_entity_id: row.user_count for row in result}




