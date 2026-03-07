import urllib.robotparser


class State:
    def __init__(self, parser: urllib.robotparser.RobotFileParser):
        self._parser = parser
    
    @staticmethod
    def init_with_content(content: str):
        robot_file_parser = urllib.robotparser.RobotFileParser()
        robot_file_parser.parse(content.splitlines())
        robot_file_parser.set_url('')
        return State(robot_file_parser)
    
    @staticmethod
    def init_with_url(any_link: str):
        import urllib.request
        import furl
        l_furl = furl.furl(any_link)
        l_furl.set(path='/robots.txt')
        
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/124.0.0.0 Safari/537.36"
            }
            req = urllib.request.Request(l_furl.url, headers=headers)
            with urllib.request.urlopen(req, timeout=5.0) as response:
                robots_txt_content = response.read().decode('utf-8')
            
            robot_file_parser = urllib.robotparser.RobotFileParser()
            robot_file_parser.parse(robots_txt_content.splitlines())
            robot_file_parser.set_url(l_furl.url)
            
            print('INFO: load robots.txt', {'source': l_furl.url})
            
            return robot_file_parser
        except Exception as e:
            print(f"WARN: Failed to load {l_furl.url}: {e}")
            return MockedParser()
    
    def is_disallowed(self, user_agent: str, url: str):
        return not self._parser.can_fetch(user_agent, url)
    
    def get_any(self, any_link: str) -> "urllib.robotparser.RobotFileParser | MockedParser":
        instance = self.build_parse(any_link)
        if instance is not None:
            return instance
        else:
            return MockedParser()


class MockedParser:
    def can_fetch(self, agent_name: str, url: str):
        return True  # default answer if robots.txt is not provided
