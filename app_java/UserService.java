package com.example.demo.service;

import com.example.demo.model.User;
import com.example.demo.util.EncryptionUtil;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;

@Service
public class UserService {

    private final Map<String, User> userData = new HashMap<>();
    private final BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
    private final EncryptionUtil encryptionUtil = new EncryptionUtil();

    public void register(User user) {
        user.setName(encryptionUtil.encrypt(user.getName()));
        user.setEmail(encryptionUtil.encrypt(user.getEmail()));
        user.setPassword(passwordEncoder.encode(user.getPassword()));
        user.setSsn(encryptionUtil.encrypt(user.getSsn()));
        userData.put(user.getUsername(), user);
    }

    public User getUser(String username) {
        User user = userData.get(username);
        if (user != null) {
            user.setName(encryptionUtil.decrypt(user.getName()));
            user.setEmail(encryptionUtil.decrypt(user.getEmail()));
            user.setSsn(encryptionUtil.decrypt(user.getSsn()));
        }
        return user;
    }
}
