from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, Float, Date
import enum

Base = declarative_base()

class Ineqs(enum.Enum):
    gte = ">="
    gt = ">"
    lte = "<="
    lt = "<"
    eq = "=="

class Units(enum.Enum):
    php = "php"
    count = "count"

class Prio(enum.Enum):
    low = "LOW"
    medium = "MEDIUM"
    high = "HIGH"


class AlertRule(Base):
    __tablename__ = "alert_rules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    domain = Column(String)
    inequality = Column(Enum(Ineqs))
    threshold = Column(Float)
    unit = Column(Enum(Units))

class Cca(Base):
    __tablename__ = "clustered_alerts"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String)
    priority = Column(Enum(Prio))
    email = Column(String)
    date_from = Column(Date)
    date_to = Column(Date)

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_rule_id = Column(Integer)
    alert_rule_name = Column(String)
    user_id = Column(String)
    email = Column(String)
    transaction_id = Column(String)
    related_transactions = Column(JSONB)

# class FiatOutIndivRank(Base):
#     __tablename__ = "fiat_out_ranking"

#     user_id = Column(Integer)
#     email = Column(String)
#     rank = Column(Integer)
#     txn_volume_php = Column(Float)
#     txn_volume_count = Column(Integer)

# class FiatInIndivRank(Base):
#     __tablename__ = "fiat_in_ranking"

#     user_id = Column(Integer)
#     email = Column(String)
#     rank = Column(Integer)
#     txn_volume_php = Column(Float)
#     txn_volume_count = Column(Integer)

# class CryptoOutIndivRank(Base):
#     __tablename__ = "crypto_out_ranking"

#     user_id = Column(Integer)
#     email = Column(String)
#     rank = Column(Integer)
#     txn_volume_php = Column(Float)
#     txn_volume_count = Column(Integer)

# class CryptoInIndivRank(Base):
#     __tablename__ = "crypto_in_ranking"

#     user_id = Column(Integer)
#     email = Column(String)
#     rank = Column(Integer)
#     txn_volume_php = Column(Float)
#     txn_volume_count = Column(Integer)

# class TradeRank(Base):
#     __tablename__ = "trade_ranking"

#     user_id = Column(Integer)
#     email = Column(String)
#     rank = Column(Integer)
#     txn_volume_php = Column(Float)
#     txn_volume_count = Column(Integer)