package lk.dilan.project.apigateway.util;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import org.springframework.stereotype.Component;

@Component
public class JwtUtil {

    public void validateToken(final String token) {
        try {
            String[] chunks = token.split("\\.");
            if (chunks.length < 2) {
                throw new RuntimeException("Invalid Token Format");
            }
        } catch (Exception e) {
            System.out.println("❌ Token Error: " + e.getMessage());
            throw new RuntimeException("Unauthorized access");
        }
    }
}