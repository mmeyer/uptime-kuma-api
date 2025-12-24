# Create DTO Object for easier monitor creation

from typing import Optional
from .monitor_type import MonitorType
from .auth_method import AuthMethod


class MonitorBuilder:
    """Builder pattern for creating monitor configurations."""
    
    def __init__(self):
        self._data = {}
    
    # Core attributes
    def with_type(self, value: MonitorType) -> 'MonitorBuilder':
        self._data['type'] = value
        return self
    
    def with_name(self, value: str) -> 'MonitorBuilder':
        self._data['name'] = value
        return self
    
    def with_parent(self, value: Optional[int]) -> 'MonitorBuilder':
        self._data['parent'] = value
        return self
    
    def with_description(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['description'] = value
        return self
    
    def with_interval(self, value: int = 60) -> 'MonitorBuilder':
        self._data['interval'] = value
        return self
    
    def with_retry_interval(self, value: int = 60) -> 'MonitorBuilder':
        self._data['retryInterval'] = value
        return self
    
    def with_resend_interval(self, value: int = 0) -> 'MonitorBuilder':
        self._data['resendInterval'] = value
        return self
    
    def with_maxretries(self, value: int = 1) -> 'MonitorBuilder':
        self._data['maxretries'] = value
        return self
    
    def with_upside_down(self, value: bool = False) -> 'MonitorBuilder':
        self._data['upsideDown'] = value
        return self
    
    def with_notification_id_list(self, value: Optional[list]) -> 'MonitorBuilder':
        self._data['notificationIDList'] = value
        return self
    
    def with_http_body_encoding(self, value: str = "json") -> 'MonitorBuilder':
        self._data['httpBodyEncoding'] = value
        return self
    
    # HTTP, KEYWORD, JSON_QUERY, REAL_BROWSER
    def with_url(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['url'] = value
        return self
    
    # HTTP, KEYWORD, GRPC_KEYWORD
    def with_maxredirects(self, value: int = 10) -> 'MonitorBuilder':
        self._data['maxredirects'] = value
        return self
    
    def with_accepted_statuscodes(self, value: Optional[list[str]]) -> 'MonitorBuilder':
        self._data['accepted_statuscodes'] = value
        return self
    
    # HTTP, KEYWORD, JSON_QUERY
    def with_expiry_notification(self, value: bool = False) -> 'MonitorBuilder':
        self._data['expiryNotification'] = value
        return self
    
    def with_ignore_tls(self, value: bool = False) -> 'MonitorBuilder':
        self._data['ignoreTls'] = value
        return self
    
    def with_proxy_id(self, value: Optional[int]) -> 'MonitorBuilder':
        self._data['proxyId'] = value
        return self
    
    def with_method(self, value: str = "GET") -> 'MonitorBuilder':
        self._data['method'] = value
        return self
    
    def with_body(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['body'] = value
        return self
    
    def with_headers(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['headers'] = value
        return self
    
    def with_auth_method(self, value: AuthMethod = AuthMethod.NONE) -> 'MonitorBuilder':
        self._data['authMethod'] = value
        return self
    
    def with_tls_cert(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['tlsCert'] = value
        return self
    
    def with_tls_key(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['tlsKey'] = value
        return self
    
    def with_tls_ca(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['tlsCa'] = value
        return self
    
    def with_basic_auth_user(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['basic_auth_user'] = value
        return self
    
    def with_basic_auth_pass(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['basic_auth_pass'] = value
        return self
    
    def with_auth_domain(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['authDomain'] = value
        return self
    
    def with_auth_workstation(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['authWorkstation'] = value
        return self
    
    def with_oauth_auth_method(self, value: str = "client_secret_basic") -> 'MonitorBuilder':
        self._data['oauth_auth_method'] = value
        return self
    
    def with_oauth_token_url(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['oauth_token_url'] = value
        return self
    
    def with_oauth_client_id(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['oauth_client_id'] = value
        return self
    
    def with_oauth_client_secret(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['oauth_client_secret'] = value
        return self
    
    def with_oauth_scopes(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['oauth_scopes'] = value
        return self
    
    def with_timeout(self, value: int = 48) -> 'MonitorBuilder':
        self._data['timeout'] = value
        return self
    
    # KEYWORD
    def with_keyword(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['keyword'] = value
        return self
    
    def with_invert_keyword(self, value: bool = False) -> 'MonitorBuilder':
        self._data['invertKeyword'] = value
        return self
    
    # GRPC_KEYWORD
    def with_grpc_url(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['grpcUrl'] = value
        return self
    
    def with_grpc_enable_tls(self, value: bool = False) -> 'MonitorBuilder':
        self._data['grpcEnableTls'] = value
        return self
    
    def with_grpc_service_name(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['grpcServiceName'] = value
        return self
    
    def with_grpc_method(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['grpcMethod'] = value
        return self
    
    def with_grpc_protobuf(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['grpcProtobuf'] = value
        return self
    
    def with_grpc_body(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['grpcBody'] = value
        return self
    
    def with_grpc_metadata(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['grpcMetadata'] = value
        return self
    
    # PORT, PING, DNS, STEAM, MQTT, RADIUS, TAILSCALE_PING
    def with_hostname(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['hostname'] = value
        return self
    
    # PING
    def with_packet_size(self, value: int = 56) -> 'MonitorBuilder':
        self._data['packetSize'] = value
        return self
    
    # PORT, DNS, STEAM, MQTT, RADIUS
    def with_port(self, value: Optional[int]) -> 'MonitorBuilder':
        self._data['port'] = value
        return self
    
    # DNS
    def with_dns_resolve_server(self, value: str = "1.1.1.1") -> 'MonitorBuilder':
        self._data['dns_resolve_server'] = value
        return self
    
    def with_dns_resolve_type(self, value: str = "A") -> 'MonitorBuilder':
        self._data['dns_resolve_type'] = value
        return self
    
    # MQTT
    def with_mqtt_username(self, value: str = "") -> 'MonitorBuilder':
        self._data['mqttUsername'] = value
        return self
    
    def with_mqtt_password(self, value: str = "") -> 'MonitorBuilder':
        self._data['mqttPassword'] = value
        return self
    
    def with_mqtt_topic(self, value: str = "") -> 'MonitorBuilder':
        self._data['mqttTopic'] = value
        return self
    
    def with_mqtt_success_message(self, value: str = "") -> 'MonitorBuilder':
        self._data['mqttSuccessMessage'] = value
        return self
    
    # SQLSERVER, POSTGRES, MYSQL, MONGODB, REDIS
    def with_database_connection_string(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['databaseConnectionString'] = value
        return self
    
    # SQLSERVER, POSTGRES, MYSQL
    def with_database_query(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['databaseQuery'] = value
        return self
    
    # DOCKER
    def with_docker_container(self, value: str = "") -> 'MonitorBuilder':
        self._data['docker_container'] = value
        return self
    
    def with_docker_host(self, value: Optional[int]) -> 'MonitorBuilder':
        self._data['docker_host'] = value
        return self
    
    # RADIUS
    def with_radius_username(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['radiusUsername'] = value
        return self
    
    def with_radius_password(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['radiusPassword'] = value
        return self
    
    def with_radius_secret(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['radiusSecret'] = value
        return self
    
    def with_radius_called_station_id(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['radiusCalledStationId'] = value
        return self
    
    def with_radius_calling_station_id(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['radiusCallingStationId'] = value
        return self
    
    # GAMEDIG
    def with_game(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['game'] = value
        return self
    
    def with_gamedig_given_port_only(self, value: bool = True) -> 'MonitorBuilder':
        self._data['gamedigGivenPortOnly'] = value
        return self
    
    # JSON_QUERY
    def with_json_path(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['jsonPath'] = value
        return self
    
    def with_expected_value(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['expectedValue'] = value
        return self
    
    # KAFKA_PRODUCER
    def with_kafka_producer_brokers(self, value: Optional[list[str]]) -> 'MonitorBuilder':
        self._data['kafkaProducerBrokers'] = value
        return self
    
    def with_kafka_producer_topic(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['kafkaProducerTopic'] = value
        return self
    
    def with_kafka_producer_message(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['kafkaProducerMessage'] = value
        return self
    
    def with_kafka_producer_ssl(self, value: bool = False) -> 'MonitorBuilder':
        self._data['kafkaProducerSsl'] = value
        return self
    
    def with_kafka_producer_allow_auto_topic_creation(self, value: bool = False) -> 'MonitorBuilder':
        self._data['kafkaProducerAllowAutoTopicCreation'] = value
        return self
    
    def with_kafka_producer_sasl_options(self, value: Optional[dict]) -> 'MonitorBuilder':
        self._data['kafkaProducerSaslOptions'] = value
        return self
    
    # 2.0.0
    def with_mqtt_check_type(self, value: str = "keyword") -> 'MonitorBuilder':
        self._data['mqttCheckType'] = value
        return self
    
    def with_cache_bust(self, value: bool = False) -> 'MonitorBuilder':
        self._data['cacheBust'] = value
        return self
    
    def with_remote_browser(self, value) -> 'MonitorBuilder':
        self._data['remote_browser'] = value
        return self
    
    def with_json_path_operator(self, value: str = "==") -> 'MonitorBuilder':
        self._data['jsonPathOperator'] = value
        return self
    
    def with_snmp_version(self, value: str = "2c") -> 'MonitorBuilder':
        self._data['snmpVersion'] = value
        return self
    
    def with_rabbitmq_nodes(self, value: Optional[list]) -> 'MonitorBuilder':
        self._data['rabbitmqNodes'] = value
        return self
    
    def with_conditions(self, value: Optional[list]) -> 'MonitorBuilder':
        self._data['conditions'] = value
        return self
    
    def with_ip_family(self, value) -> 'MonitorBuilder':
        self._data['ipFamily'] = value
        return self
    
    def with_ping_numeric(self, value: bool = True) -> 'MonitorBuilder':
        self._data['ping_numeric'] = value
        return self
    
    def with_ping_count(self, value: int = 3) -> 'MonitorBuilder':
        self._data['ping_count'] = value
        return self
    
    def with_ping_per_request_timeout(self, value: int = 2) -> 'MonitorBuilder':
        self._data['ping_per_request_timeout'] = value
        return self
    
    def with_mqtt_websocket_path(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['mqttWebsocketPath'] = value
        return self
    
    def with_rabbitmq_username(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['rabbitmqUsername'] = value
        return self
    
    def with_rabbitmq_password(self, value: Optional[str]) -> 'MonitorBuilder':
        self._data['rabbitmqPassword'] = value
        return self
    
    def build(self) -> dict:
        """Build and return the monitor configuration dictionary."""
        return self._data.copy()

    @staticmethod
    def create_monitor() -> 'MonitorBuilder':
        """Factory function to create a new MonitorBuilder instance."""
        return MonitorBuilder()
