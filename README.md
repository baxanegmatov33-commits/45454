```mermaid
flowchart TD
    %% ==========================
    %% Key Generator
    %% ==========================
    subgraph Key_Generator["Key Generator"]
        A1[Start] --> A2[Generate RSA private key 2048 bits]
        A2 --> A3[Extract public key from private key]
        A3 --> A4[Save private key to private_key.pem]
        A4 --> A5[Save public key to public_key.pem]
        A5 --> A6[Print KEY GENERATION OK]
        A6 --> A7[End]
    end

    %% ==========================
    %% Signer
    %% ==========================
    subgraph Signer["Signer"]
        B1[Start] --> B2[Input message from user]
        B2 --> B3[Load private key from private_key.pem]
        B3 --> B4[Hash message with SHA-256]
        B4 --> B5[Sign hash with RSA private key]
        B5 --> B6[Save signature to signature.sig]
        B6 --> B7[Print SIGNATURE CREATED OK]
        B7 --> B8[End]
    end

    %% ==========================
    %% Signature Verifier
    %% ==========================
    subgraph Verifier["Signature Verifier"]
        C1[Start] --> C2[Input message from user]
        C2 --> C3[Load public key from public_key.pem]
        C3 --> C4[Load signature from signature.sig]
        C4 --> C5[Verify signature with RSA + SHA-256]
        C5 --> C6{Signature valid?}
        C6 -->|Yes| C7[Print SIGNATURE VALID]
        C6 -->|No| C8[Print SIGNATURE INVALID]
        C7 --> C9[End]
        C8 --> C9
    end

    %% ==========================
    %% Connections between programs
    %% ==========================
    A5 --> B3
    B6 --> C4
